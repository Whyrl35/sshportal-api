from flask_restful import Resource  # , reqparse
from flask_jwt_extended import jwt_required
from run import api
from .models import AclsModel, HostGroupAclsModel, HostGroupsModel, UserGroupAclModel, UserGroupsModel


class Acls(Resource):
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
