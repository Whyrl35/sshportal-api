from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import HostGroupsModel, HostGroupAclsModel, AclsModel, HostHostGroupsModel, HostsModel


class HostGroups(Resource):
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
