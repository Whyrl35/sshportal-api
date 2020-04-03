from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import HostsModel, SshKeysModel


class Keys(Resource):
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
