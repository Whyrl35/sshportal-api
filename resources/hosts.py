from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import HostGroupsModel, HostHostGroupsModel, HostsModel, SshKeysModel


class Hosts(Resource):
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
