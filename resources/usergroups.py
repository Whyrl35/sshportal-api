from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import UserGroupsModel, UserUserGroupsModel, UserModel, UserGroupAclModel, AclsModel


class UserGroups(Resource):
    @jwt_required
    def get(self):
        usergroups_json = []
        usergroups = UserGroupsModel.return_all()

        for usergroup in usergroups:
            usergroups_part = UserGroupsModel.to_json(usergroup)
            usergroups_json.append(usergroups_part)

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

        return usergroups_json


api.add_resource(UserGroups, '/v1/usergroups')
