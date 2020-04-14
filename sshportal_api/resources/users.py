# from flasgger import swag_from
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
from sshportal_api import api
from sshportal_api.models import UserModel, RevokedTokenModel
from flask_restful_swagger_3 import swagger
import datetime


parser = reqparse.RequestParser()
parser.add_argument('name', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class Registration(Resource):
    @swagger.doc({
        'tags': ['user'],
        'description': "Register a new user",
        'responses': {
            '200': {
                'description': "Register a new user",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {}
                        }
                    }
                }
            },
            '401': {
                'description': "Your are not authorized to register the user",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {}
                        }
                    }
                }
            },
            '500': {
                'description': "Failed to register the user",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {}
                        }
                    }
                }
            }
        }
    })
    def post(self):

        if request.remote_addr != '127.0.0.1':
            return {'message': "Your are'nt authorized to access this route"}, 401

        data = parser.parse_args()

        if UserModel.find_by_name(data['name']):
            return {'message': 'User {} already exists'.format(data['name'])}

        new_user = UserModel(
            name=data['name'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['name'], expires_delta=datetime.timedelta(hours=1))
            refresh_token = create_refresh_token(identity=data['name'])
            return {
                'message': 'User {} was created'.format(data['name']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500


class Login(Resource):
    @swagger.doc({
        'tags': ['user'],
        'description': "Login a user",
        'parameters': [
            {
                'name': 'name',
                'description': 'the name of the user',
                'in': 'query',
                'schema': {'type': 'string'}
            },
            {
                'name': 'password',
                'description': 'the password of the user',
                'in': 'query',
                'schema': {'type': 'password'}
            }
        ],
        'responses': {
            '200': {
                'description': "Login a user",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "message": "Logged in as ludovic",
                                "user": "ludovic",
                                "access_token": "eyJ0....6g",
                                "refresh_token": "eyJ0....74"
                            }
                        }
                    }
                }
            },
            '401': {
                'description': "Your are not authorized to register the user",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "message": "Wrong credentials"
                            }
                        }
                    }
                }
            }
        }
    })
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_name(data['name'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['name'])}, 400

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['name'], expires_delta=datetime.timedelta(hours=1))
            refresh_token = create_refresh_token(identity=data['name'])
            return {
                'message': 'Logged in as {}'.format(current_user.name),
                'user': current_user.name,
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 200, {'jwt-token': access_token}
        else:
            return {'message': 'Wrong credentials'}, 401


class LogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class LogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        try:
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user, expires_delta=datetime.timedelta(hours=1))
            return {'access_token': access_token}, 200, {'jwt-token': access_token}
        except:
            return {'message': 'Your not authorized.'}, 401


class DevToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        if request.remote_addr != '127.0.0.1':
            return {'message': "Your are'nt authorized to access this route"}, 401

        try:
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user, expires_delta=False)
            return {'access_token': access_token}
        except:
            return {'message': 'Your not authorized.'}, 401


class AllUsers(Resource):
    @jwt_required
    def get(self):
        return UserModel.return_all()


class User(Resource):
    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        current_user = UserModel.find_by_name(data['name'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['name'])}, 400

        return UserModel.to_json(current_user)


#
# Adding resources:
api.add_resource(Registration, '/v1/private/registration')
api.add_resource(DevToken, '/v1/private/devtoken')

api.add_resource(Login, '/v1/login')
api.add_resource(AllUsers, '/v1/users')
api.add_resource(User, '/v1/user')
api.add_resource(TokenRefresh, '/v1/token')
api.add_resource(LogoutAccess, '/v1/logout/access')
api.add_resource(LogoutRefresh, '/v1/logout/refresh')
