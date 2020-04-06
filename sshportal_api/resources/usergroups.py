from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import UserGroupsModel, UserUserGroupsModel, UserModel, UserGroupAclModel, AclsModel


class UserGroups(Resource):
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
