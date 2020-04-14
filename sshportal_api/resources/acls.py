from flask_restful import Resource  # , reqparse
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import AclsModel, HostGroupAclsModel, HostGroupsModel, UserGroupAclModel, UserGroupsModel
from flask_restful_swagger_3 import swagger


class Acls(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['acl'],
        'description': "Return list of acls",
        'responses': {
            '200': {
                'description': "A list of acls",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.484494",
                                    "updated_at": "2019-11-13T16:08:45.484494",
                                    "deleted_at": None,
                                    "host_pattern": "",
                                    "action": "allow",
                                    "weight": 0,
                                    "comment": "created by sshportal",
                                    "host_groups": {
                                        "id": 1,
                                        "created_at": "2019-11-13T16:08:45.476325",
                                        "updated_at": "2019-11-13T16:08:45.485020",
                                        "deleted_at": None,
                                        "name": "default",
                                        "comment": "created by sshportal"
                                    },
                                    "user_groups": {
                                        "id": 1,
                                        "created_at": "2019-11-13T16:08:45.480323",
                                        "updated_at": "2019-11-13T16:08:45.491408",
                                        "deleted_at": None,
                                        "name": "default",
                                        "comment": "created by sshportal"
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
        acls_json = []
        acls = AclsModel.return_all()
        for acl in acls:
            acl_part = AclsModel.to_json(acl)
            host_group_acls = HostGroupAclsModel.by_acl_id(acl.id)
            host_group = HostGroupsModel.by_id(host_group_acls.host_group_id)
            acl_part['host_groups'] = HostGroupsModel.to_json(host_group)
            user_group_acls = UserGroupAclModel.by_acl_id(acl.id)
            user_group = UserGroupsModel.by_id(user_group_acls.user_group_id)
            acl_part['user_groups'] = UserGroupsModel.to_json(user_group)
            acls_json.append(acl_part)

        return acls_json


class Acl(Resource):
    @swagger.doc({
        'tags': ['acl'],
        'description': "Return an acl that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of an acl',
                'in': 'path',
                'schema': {
                    'type': 'integer',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The acl that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "id": 1,
                                "created_at": "2019-11-13T16:08:45.484494",
                                "updated_at": "2019-11-13T16:08:45.484494",
                                "deleted_at": None,
                                "host_pattern": "",
                                "action": "allow",
                                "weight": 0,
                                "comment": "created by sshportal",
                                "host_groups": {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.476325",
                                    "updated_at": "2019-11-13T16:08:45.485020",
                                    "deleted_at": None,
                                    "name": "default",
                                    "comment": "created by sshportal"
                                },
                                "user_groups": {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.480323",
                                    "updated_at": "2019-11-13T16:08:45.491408",
                                    "deleted_at": None,
                                    "name": "default",
                                    "comment": "created by sshportal"
                                }
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        # parser = reqparse.RequestParser()
        # parser.add_argument('id', help='This field cannot be blank', required=True)
        # data = parser.parse_args()

        # acl = AclsModel.by_id(data['id'])
        acl = AclsModel.by_id(id)
        acl_part = AclsModel.to_json(acl)
        host_group_acls = HostGroupAclsModel.by_acl_id(acl.id)
        host_group = HostGroupsModel.by_id(host_group_acls.host_group_id)
        acl_part['host_groups'] = HostGroupsModel.to_json(host_group)
        user_group_acls = UserGroupAclModel.by_acl_id(acl.id)
        user_group = UserGroupsModel.by_id(user_group_acls.user_group_id)
        acl_part['user_groups'] = UserGroupsModel.to_json(user_group)

        return acl_part


api.add_resource(Acls, '/v1/acls')
api.add_resource(Acl, '/v1/acl/<int:id>')
