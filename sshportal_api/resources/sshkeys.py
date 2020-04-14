from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import HostsModel, SshKeysModel
from flask_restful_swagger_3 import swagger


class Keys(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['key'],
        'description': "Return list of keys",
        'responses': {
            '200': {
                'description': "A list of keys",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.471568",
                                    "updated_at": "2019-11-13T16:08:45.471568",
                                    "deleted_at": None,
                                    "name": "default",
                                    "type": "rsa",
                                    "length": 2048,
                                    "fingerprint": "",
                                    "priv_key": "-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n",  # noqa
                                    "pub_key": "ssh-rsa AAAAB3N.........Ez",
                                    "comment": "created by sshportal",
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
        keys_json = []
        keys = SshKeysModel.return_all()
        for key in keys:
            keys_part = SshKeysModel.to_json(key)

            keys_part['hosts'] = []
            hosts = HostsModel.by_ssh_key_id(key.id)
            for host in hosts:
                keys_part['hosts'].append(HostsModel.to_json(host))

            keys_json.append(keys_part)

        return keys_json


class KeyId(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['key'],
        'description': "Return a key that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a key',
                'in': 'path',
                'schema': {'type': 'integer'}
            }
        ],
        'responses': {
            '200': {
                'description': "The key that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            "id": 1,
                            "created_at": "2019-11-13T16:08:45.471568",
                            "updated_at": "2019-11-13T16:08:45.471568",
                            "deleted_at": None,
                            "name": "default",
                            "type": "rsa",
                            "length": 2048,
                            "fingerprint": "",
                            "priv_key": "-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n",
                            "pub_key": "ssh-rsa AAAAB3N.........Ez",
                            "comment": "created by sshportal",
                            "hosts": []
                        },
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        key = SshKeysModel.by_id(id)
        keys_part = SshKeysModel.to_json(key)

        keys_part['hosts'] = []
        hosts = HostsModel.by_ssh_key_id(key.id)
        for host in hosts:
            keys_part['hosts'].append(HostsModel.to_json(host))

        return keys_part


class KeyName(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['key'],
        'description': "Return a key that match the given name",
        'parameters': [
            {
                'name': 'name',
                'description': 'the name of a key',
                'in': 'path',
                'schema': {'type': 'integer'}
            }
        ],
        'responses': {
            '200': {
                'description': "The key that match the name",
                'content': {
                    'application/json': {
                        'examples': {
                            "id": 1,
                            "created_at": "2019-11-13T16:08:45.471568",
                            "updated_at": "2019-11-13T16:08:45.471568",
                            "deleted_at": None,
                            "name": "default",
                            "type": "rsa",
                            "length": 2048,
                            "fingerprint": "",
                            "priv_key": "-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n",
                            "pub_key": "ssh-rsa AAAAB3N.........Ez",
                            "comment": "created by sshportal",
                            "hosts": []
                        },
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, name):
        key = SshKeysModel.by_name(name)
        keys_part = SshKeysModel.to_json(key)

        keys_part['hosts'] = []
        hosts = HostsModel.by_ssh_key_id(key.id)
        for host in hosts:
            keys_part['hosts'].append(HostsModel.to_json(host))

        return keys_part


api.add_resource(Keys, '/v1/keys')
api.add_resource(KeyId, '/v1/key/<int:id>')
api.add_resource(KeyName, '/v1/key/<string:name>')
