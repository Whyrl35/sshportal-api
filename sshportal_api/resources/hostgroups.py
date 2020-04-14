from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import HostGroupsModel, HostGroupAclsModel, AclsModel, HostHostGroupsModel, HostsModel
from flask_restful_swagger_2 import swagger


class HostGroups(Resource):
    @swagger.doc({
        'tags': ['hostgroup'],
        'description': "Return list of hostgroups",
        'responses': {
            '200': {
                'description': "A list of hostgroups",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.476325",
                                    "updated_at": "2019-11-13T16:08:45.485020",
                                    "deleted_at": None,
                                    "name": "default",
                                    "comment": "created by sshportal",
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
                                    ],
                                    "hosts": []
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
        host_groups_json = []
        host_groups = HostGroupsModel.return_all()
        for host_group in host_groups:
            host_groups_part = HostGroupsModel.to_json(host_group)

            host_group_acls = HostGroupAclsModel.by_host_group_id(host_group.id)
            host_groups_part['acls'] = []
            for hgacls in host_group_acls:
                acl = AclsModel.by_id(hgacls.acl_id)
                host_groups_part['acls'].append(AclsModel.to_json(acl))

            host_host_groups = HostHostGroupsModel.by_host_group_id(host_group.id)
            host_groups_part['hosts'] = []
            for hhg in host_host_groups:
                host = HostsModel.by_id(hhg.host_id)
                host_groups_part['hosts'].append(HostsModel.to_json(host) if host else None)

            host_groups_json.append(host_groups_part)

        return host_groups_json


class HostGroupId(Resource):
    @swagger.doc({
        'tags': ['hostgroup'],
        'description': "Return a hostgroup that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a hostgroup',
                'in': 'path',
                'schema': {
                    'type': 'integer',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The hostgroup that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "id": 1,
                                "created_at": "2019-11-13T16:08:45.476325",
                                "updated_at": "2019-11-13T16:08:45.485020",
                                "deleted_at": None,
                                "name": "default",
                                "comment": "created by sshportal",
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
                                ],
                                "hosts": []
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        host_group = HostGroupsModel.by_id(id)
        host_groups_part = HostGroupsModel.to_json(host_group)

        host_group_acls = HostGroupAclsModel.by_host_group_id(host_group.id)
        host_groups_part['acls'] = []
        for hgacls in host_group_acls:
            acl = AclsModel.by_id(hgacls.acl_id)
            host_groups_part['acls'].append(AclsModel.to_json(acl))

        host_host_groups = HostHostGroupsModel.by_host_group_id(host_group.id)
        host_groups_part['hosts'] = []
        for hhg in host_host_groups:
            host = HostsModel.by_id(hhg.host_id)
            host_groups_part['hosts'].append(HostsModel.to_json(host) if host else None)

        return host_groups_part


class HostGroupName(Resource):
    @swagger.doc({
        'tags': ['hostgroup'],
        'description': "Return a hostgroup that match the given name",
        'parameters': [
            {
                'name': 'name',
                'description': 'the name of a hostgroup',
                'in': 'path',
                'schema': {
                    'type': 'string',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The hostgroup that match the name",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "id": 1,
                                "created_at": "2019-11-13T16:08:45.476325",
                                "updated_at": "2019-11-13T16:08:45.485020",
                                "deleted_at": None,
                                "name": "default",
                                "comment": "created by sshportal",
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
                                ],
                                "hosts": []
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, name):
        host_group = HostGroupsModel.by_name(name)
        host_groups_part = HostGroupsModel.to_json(host_group)

        host_group_acls = HostGroupAclsModel.by_host_group_id(host_group.id)
        host_groups_part['acls'] = []
        for hgacls in host_group_acls:
            acl = AclsModel.by_id(hgacls.acl_id)
            host_groups_part['acls'].append(AclsModel.to_json(acl))

        host_host_groups = HostHostGroupsModel.by_host_group_id(host_group.id)
        host_groups_part['hosts'] = []
        for hhg in host_host_groups:
            host = HostsModel.by_id(hhg.host_id)
            host_groups_part['hosts'].append(HostsModel.to_json(host) if host else None)

        return host_groups_part


api.add_resource(HostGroups, '/v1/host_groups')
api.add_resource(HostGroupId, '/v1/host_group/<int:id>')
api.add_resource(HostGroupName, '/v1/host_group/<string:name>')
