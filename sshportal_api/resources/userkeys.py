from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import UserKeysModel, UserModel
from flask_restful_swagger_2 import swagger


class UserKeys(Resource):
    @swagger.doc({
        'tags': ['userkey'],
        'description': "Return list of userkeys",
        'responses': {
            '200': {
                'description': "A list of userkeys",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:13:13.088607",
                                    "updated_at": "2019-11-13T16:13:13.088607",
                                    "deleted_at": None,
                                    "key": "AAAAB3N.......==",
                                    "user_id": 1,
                                    "comment": "created by sshportal",
                                    "authorized_key": "ssh-rsa AAAAB3N.......==\n",
                                    "user": {
                                        "id": 1,
                                        "name": "admin",
                                        "password": None,
                                        "created_at": "2019-11-13T16:08:45.490830",
                                        "updated_at": "2019-11-13T16:39:21.114928",
                                        "deleted_at": None,
                                        "is_admin": None,
                                        "email": "admin@localhost",
                                        "comment": "created by sshportal",
                                        "invite_token": "1234567890"
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self):
        userkeys_json = []
        userkeys = UserKeysModel.return_all()

        for userkey in userkeys:
            userkeys_part = UserKeysModel.to_json(userkey)

            user = UserModel.by_id(userkey.user_id)
            userkeys_part['user'] = UserModel.to_json(user)

            userkeys_json.append(userkeys_part)

        return userkeys_json


class UserKey(Resource):
    @swagger.doc({
        'tags': ['userkey'],
        'description': "Return a userkey that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a userkey',
                'in': 'path',
                'schema': {'type': 'integer'}
            }
        ],
        'responses': {
            '200': {
                'description': "The userkey that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            "id": 1,
                            "created_at": "2019-11-13T16:13:13.088607",
                            "updated_at": "2019-11-13T16:13:13.088607",
                            "deleted_at": None,
                            "key": "AAAAB3N.......==",
                            "user_id": 1,
                            "comment": "created by sshportal",
                            "authorized_key": "ssh-rsa AAAAB3N.......==\n",
                            "user": {
                                "id": 1,
                                "name": "admin",
                                "password": None,
                                "created_at": "2019-11-13T16:08:45.490830",
                                "updated_at": "2019-11-13T16:39:21.114928",
                                "deleted_at": None,
                                "is_admin": None,
                                "email": "admin@localhost",
                                "comment": "created by sshportal",
                                "invite_token": "1234567890"
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        userkey = UserKeysModel.by_id(id)

        userkeys_part = UserKeysModel.to_json(userkey)

        user = UserModel.by_id(userkey.user_id)
        userkeys_part['user'] = UserModel.to_json(user)

        return userkeys_part


api.add_resource(UserKeys, '/v1/userkeys')
api.add_resource(UserKey, '/v1/userkey/<int:id>')
