from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import UserGroupsModel, UserUserGroupsModel, UserModel, UserGroupAclModel, AclsModel
from flask_restful_swagger_3 import swagger


class UserGroups(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['usergroup'],
        'description': "Return list of usergroups",
        'responses': {
            '200': {
                'description': "A list of usergroups",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.480323",
                                    "updated_at": "2019-11-13T16:08:45.491408",
                                    "deleted_at": None,
                                    "name": "default",
                                    "comment": "created by sshportal",
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
                                            "invite_token": "1234567890"
                                        }
                                    ],
                                    "acls": [
                                        {
                                            "id": 1,
                                            "created_at": "2019-11-13T16:08:45.484494",
                                            "updated_at": "2019-11-13T16:08:45.484494",
                                            "deleted_at": None,
                                            "host_pattern": "",
                                            "action": "allow",
                                            "weight": 0,
                                            "comment": "created by sshportal"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self):
        usergroups_json = []
        usergroups = UserGroupsModel.return_all()

        for usergroup in usergroups:
            usergroups_part = UserGroupsModel.to_json(usergroup)

            userusergroups = UserUserGroupsModel.by_user_group_id(usergroup.id)
            usergroups_part['users'] = []
            for uug in userusergroups:
                user = UserModel.by_id(uug.user_id)
                usergroups_part['users'].append(UserModel.to_json(user))

            usergroupacls = UserGroupAclModel.by_user_group_id(usergroup.id)
            usergroups_part['acls'] = []
            for uga in usergroupacls:
                acl = AclsModel.by_id(uga.acl_id)
                usergroups_part['acls'].append(AclsModel.to_json(acl))

            usergroups_json.append(usergroups_part)

        return usergroups_json


class UserGroupId(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['usergroup'],
        'description': "Return a usergroup that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a usergroup',
                'in': 'path',
                'schema': {'type': 'integer'}
            }
        ],
        'responses': {
            '200': {
                'description': "The usergroup that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            "id": 1,
                            "created_at": "2019-11-13T16:08:45.480323",
                            "updated_at": "2019-11-13T16:08:45.491408",
                            "deleted_at": None,
                            "name": "default",
                            "comment": "created by sshportal",
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
                                    "invite_token": "1234567890"
                                }
                            ],
                            "acls": [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.484494",
                                    "updated_at": "2019-11-13T16:08:45.484494",
                                    "deleted_at": None,
                                    "host_pattern": "",
                                    "action": "allow",
                                    "weight": 0,
                                    "comment": "created by sshportal"
                                }
                            ]
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        usergroup = UserGroupsModel.by_id(id)

        usergroups_part = UserGroupsModel.to_json(usergroup)

        userusergroups = UserUserGroupsModel.by_user_group_id(usergroup.id)
        usergroups_part['users'] = []
        for uug in userusergroups:
            user = UserModel.by_id(uug.user_id)
            usergroups_part['users'].append(UserModel.to_json(user))

        usergroupacls = UserGroupAclModel.by_user_group_id(usergroup.id)
        usergroups_part['acls'] = []
        for uga in usergroupacls:
            acl = AclsModel.by_id(uga.acl_id)
            usergroups_part['acls'].append(AclsModel.to_json(acl))

        return usergroups_part


class UserGroupName(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['usergroup'],
        'description': "Return a usergroup that match the given name",
        'parameters': [
            {
                'name': 'name',
                'description': 'the name of a usergroup',
                'in': 'path',
                'schema': {'type': 'string'}
            }
        ],
        'responses': {
            '200': {
                'description': "The usergroup that match the name",
                'content': {
                    'application/json': {
                        'examples': {
                            "id": 1,
                            "created_at": "2019-11-13T16:08:45.480323",
                            "updated_at": "2019-11-13T16:08:45.491408",
                            "deleted_at": None,
                            "name": "default",
                            "comment": "created by sshportal",
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
                                    "invite_token": "1234567890"
                                }
                            ],
                            "acls": [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.484494",
                                    "updated_at": "2019-11-13T16:08:45.484494",
                                    "deleted_at": None,
                                    "host_pattern": "",
                                    "action": "allow",
                                    "weight": 0,
                                    "comment": "created by sshportal"
                                }
                            ]
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, name):
        usergroup = UserGroupsModel.by_name(name)

        usergroups_part = UserGroupsModel.to_json(usergroup)

        userusergroups = UserUserGroupsModel.by_user_group_id(usergroup.id)
        usergroups_part['users'] = []
        for uug in userusergroups:
            user = UserModel.by_id(uug.user_id)
            usergroups_part['users'].append(UserModel.to_json(user))

        usergroupacls = UserGroupAclModel.by_user_group_id(usergroup.id)
        usergroups_part['acls'] = []
        for uga in usergroupacls:
            acl = AclsModel.by_id(uga.acl_id)
            usergroups_part['acls'].append(AclsModel.to_json(acl))

        return usergroups_part


api.add_resource(UserGroups, '/v1/usergroups')
api.add_resource(UserGroupId, '/v1/usergroup/<int:id>')
api.add_resource(UserGroupName, '/v1/usergroup/<string:name>')
