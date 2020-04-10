from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import UserModel, UserRolesModel, UserUserRolesModel
from flask_restful_swagger_2 import swagger


class UserRoles(Resource):
    @swagger.doc({
        'tags': ['userroles'],
        'description': "Return list of userroles",
        'responses': {
            '200': {
                'description': "A list of userroles",
                'examples': {
                    'application/json': [
                        {
                            "id": 1,
                            "created_at": "2019-11-13T16:08:45.263598",
                            "updated_at": "2019-11-13T16:31:34.940968",
                            "deleted_at": None,
                            "name": "admin",
                            "users": [
                                {
                                    "id": 1,
                                    "name": "admin",
                                    "password": None,
                                    "created_at": "2019-11-13T16:08:45.490830",
                                    "updated_at": "2019-11-13T16:39:21.114928",
                                    "deleted_at": None,
                                    "is_admin": None,
                                    "email": "admin@localhost",
                                    "comment": "created by sshportal",
                                    "invite_token": "711pl82xwUJ4CCFw"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    })
    @jwt_required
    def get(self):
        userroles_json = []
        userroles = UserRolesModel.return_all()

        for userrole in userroles:
            userroles_part = UserRolesModel.to_json(userrole)

            useruserroles = UserUserRolesModel.by_user_role_id(userrole.id)
            userroles_part['users'] = []
            for uur in useruserroles:
                user = UserModel.by_id(uur.user_id)
                userroles_part['users'].append(UserModel.to_json(user))

            userroles_json.append(userroles_part)

        return userroles_json


class UserRoleId(Resource):
    @swagger.doc({
        'tags': ['userrole'],
        'description': "Return a userrole that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a userrole',
                'in': 'path',
                'type': 'integer',
            }
        ],
        'responses': {
            '200': {
                'description': "The userrole that match the ID",
                'examples': {
                    "id": 1,
                    "created_at": "2019-11-13T16:08:45.263598",
                    "updated_at": "2019-11-13T16:31:34.940968",
                    "deleted_at": None,
                    "name": "admin",
                    "users": [
                        {
                            "id": 1,
                            "name": "admin",
                            "password": None,
                            "created_at": "2019-11-13T16:08:45.490830",
                            "updated_at": "2019-11-13T16:39:21.114928",
                            "deleted_at": None,
                            "is_admin": None,
                            "email": "admin@localhost",
                            "comment": "created by sshportal",
                            "invite_token": "711pl82xwUJ4CCFw"
                        }
                    ]
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        userrole = UserRolesModel.by_id(id)

        userroles_part = UserRolesModel.to_json(userrole)

        useruserroles = UserUserRolesModel.by_user_role_id(userrole.id)
        userroles_part['users'] = []
        for uur in useruserroles:
            user = UserModel.by_id(uur.user_id)
            userroles_part['users'].append(UserModel.to_json(user))

        return userroles_part


class UserRoleName(Resource):
    @swagger.doc({
        'tags': ['userrole'],
        'description': "Return a userrole that match the given name",
        'parameters': [
            {
                'name': 'name',
                'description': 'the name of a userrole',
                'in': 'path',
                'type': 'integer',
            }
        ],
        'responses': {
            '200': {
                'description': "The userrole that match the name",
                'examples': {
                    "id": 1,
                    "created_at": "2019-11-13T16:08:45.263598",
                    "updated_at": "2019-11-13T16:31:34.940968",
                    "deleted_at": None,
                    "name": "admin",
                    "users": [
                        {
                            "id": 1,
                            "name": "admin",
                            "password": None,
                            "created_at": "2019-11-13T16:08:45.490830",
                            "updated_at": "2019-11-13T16:39:21.114928",
                            "deleted_at": None,
                            "is_admin": None,
                            "email": "admin@localhost",
                            "comment": "created by sshportal",
                            "invite_token": "711pl82xwUJ4CCFw"
                        }
                    ]
                }
            }
        }
    })
    @jwt_required
    def get(self, name):
        userrole = UserRolesModel.by_name(name)

        userroles_part = UserRolesModel.to_json(userrole)

        useruserroles = UserUserRolesModel.by_user_role_id(userrole.id)
        userroles_part['users'] = []
        for uur in useruserroles:
            user = UserModel.by_id(uur.user_id)
            userroles_part['users'].append(UserModel.to_json(user))

        return userroles_part


api.add_resource(UserRoles, '/v1/userroles')
api.add_resource(UserRoleId, '/v1/userrole/<int:id>')
api.add_resource(UserRoleName, '/v1/userrole/<string:name>')
