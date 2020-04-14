from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import HostGroupsModel, HostHostGroupsModel, HostsModel, SshKeysModel
from flask_restful_swagger_2 import swagger


class Hosts(Resource):
    @swagger.doc({
        'tags': ['host'],
        'description': "Return list of hosts",
        'responses': {
            '200': {
                'description': "A list of hostgroups",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:35:48.602836",
                                    "updated_at": "2019-11-13T16:42:17.189908",
                                    "deleted_at": None,
                                    "name": "test",
                                    "addr": "",
                                    "user": "",
                                    "password": "",
                                    "ssh_key_id": 4,
                                    "fingerprint": None,
                                    "comment": "",
                                    "host_key": "AAAA....+N",
                                    "url": "ssh://nom@test.local",
                                    "hop_ip": 0,
                                    "host_groups": {
                                        "id": 1,
                                        "created_at": "2019-11-13T16:37:47.317171",
                                        "updated_at": "2019-11-13T16:55:08.296883",
                                        "deleted_at": None,
                                        "name": "web",
                                        "comment": ""
                                    },
                                    "ssh_key": {
                                        "id": 1,
                                        "created_at": "2019-11-13T16:27:31.510282",
                                        "updated_at": "2019-11-13T17:11:42.576497",
                                        "deleted_at": None,
                                        "name": "saltstack",
                                        "type": "rsa",
                                        "length": 4096,
                                        "fingerprint": "",
                                        "priv_key": "-----BEGIN RSA PRIVATE KEY-----\n.....\n-----END RSA PRIVATE KEY-----\n",  # noqa
                                        "pub_key": "ssh-rsa AAAAB3.....NSF",
                                        "comment": "deployed by saltstack"
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
        hosts_json = []
        hosts = HostsModel.return_all()
        for host in hosts:
            hosts_part = HostsModel.to_json(host)

            host_host_groups = HostHostGroupsModel.by_host_id(host.id)
            host_group = HostGroupsModel.by_id(host_host_groups.host_group_id)
            hosts_part['host_groups'] = HostGroupsModel.to_json(host_group) if host_group else None

            ssh_key = SshKeysModel.by_id(host.ssh_key_id)
            hosts_part['ssh_key'] = SshKeysModel.to_json(ssh_key)

            hosts_json.append(hosts_part)

        return hosts_json


class HostId(Resource):
    @swagger.doc({
        'tags': ['host'],
        'description': "Return a host that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a host',
                'in': 'path',
                'schema': {
                    'type': 'integer',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The event that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "id": 1,
                                "created_at": "2019-11-13T16:35:48.602836",
                                "updated_at": "2019-11-13T16:42:17.189908",
                                "deleted_at": None,
                                "name": "test",
                                "addr": "",
                                "user": "",
                                "password": "",
                                "ssh_key_id": 4,
                                "fingerprint": None,
                                "comment": "",
                                "host_key": "AAAA....+N",
                                "url": "ssh://nom@test.local",
                                "hop_ip": 0,
                                "host_groups": {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:37:47.317171",
                                    "updated_at": "2019-11-13T16:55:08.296883",
                                    "deleted_at": None,
                                    "name": "web",
                                    "comment": ""
                                },
                                "ssh_key": {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:27:31.510282",
                                    "updated_at": "2019-11-13T17:11:42.576497",
                                    "deleted_at": None,
                                    "name": "saltstack",
                                    "type": "rsa",
                                    "length": 4096,
                                    "fingerprint": "",
                                    "priv_key": "-----BEGIN RSA PRIVATE KEY-----\n.....\n-----END RSA PRIVATE KEY-----\n",  # noqa
                                    "pub_key": "ssh-rsa AAAAB3.....NSF",
                                    "comment": "deployed by saltstack"
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
        host = HostsModel.by_id(id)
        hosts_part = HostsModel.to_json(host)

        host_host_groups = HostHostGroupsModel.by_host_id(host.id)
        host_group = HostGroupsModel.by_id(host_host_groups.host_group_id)
        hosts_part['host_groups'] = HostGroupsModel.to_json(host_group) if host_group else None

        ssh_key = SshKeysModel.by_id(host.ssh_key_id)
        hosts_part['ssh_key'] = SshKeysModel.to_json(ssh_key)

        return hosts_part


class HostName(Resource):
    @swagger.doc({
        'tags': ['host'],
        'description': "Return a host that match the given name",
        'parameters': [
            {
                'name': 'name',
                'description': 'the name of a host',
                'in': 'path',
                'schema': {
                    'type': 'integer',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The event that match the name",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "id": 1,
                                "created_at": "2019-11-13T16:35:48.602836",
                                "updated_at": "2019-11-13T16:42:17.189908",
                                "deleted_at": None,
                                "name": "test",
                                "addr": "",
                                "user": "",
                                "password": "",
                                "ssh_key_id": 4,
                                "fingerprint": None,
                                "comment": "",
                                "host_key": "AAAA....+N",
                                "url": "ssh://nom@test.local",
                                "hop_ip": 0,
                                "host_groups": {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:37:47.317171",
                                    "updated_at": "2019-11-13T16:55:08.296883",
                                    "deleted_at": None,
                                    "name": "web",
                                    "comment": ""
                                },
                                "ssh_key": {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:27:31.510282",
                                    "updated_at": "2019-11-13T17:11:42.576497",
                                    "deleted_at": None,
                                    "name": "saltstack",
                                    "type": "rsa",
                                    "length": 4096,
                                    "fingerprint": "",
                                    "priv_key": "-----BEGIN RSA PRIVATE KEY-----\n.....\n-----END RSA PRIVATE KEY-----\n",  # noqa
                                    "pub_key": "ssh-rsa AAAAB3.....NSF",
                                    "comment": "deployed by saltstack"
                                }
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, name):
        host = HostsModel.by_name(name)
        hosts_part = HostsModel.to_json(host)

        host_host_groups = HostHostGroupsModel.by_host_id(host.id)
        host_group = HostGroupsModel.by_id(host_host_groups.host_group_id)
        hosts_part['host_groups'] = HostGroupsModel.to_json(host_group) if host_group else None

        ssh_key = SshKeysModel.by_id(host.ssh_key_id)
        hosts_part['ssh_key'] = SshKeysModel.to_json(ssh_key)

        return hosts_part


api.add_resource(Hosts, '/v1/hosts')
api.add_resource(HostId, '/v1/host/<int:id>')
api.add_resource(HostName, '/v1/host/<string:name>')
