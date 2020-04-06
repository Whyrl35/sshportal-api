from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import UserModel, UserRolesModel, UserUserRolesModel


class UserRoles(Resource):
    @jwt_required
    def get(self):
        userroles_json = []
        userroles = UserRolesModel.return_all()

        for userrole in userroles:
            userroles_part = UserRolesModel.to_json(userrole)

            useruserroles = UserUserRolesModel.by_user_role_id(userrole.id)
            userroles_part['users'] = []
            for uur in useruserroles:
                user = UserModel.by_id(uur.user_id)
                userroles_part['users'].append(UserModel.to_json(user))

            userroles_json.append(userroles_part)

        return userroles_json


class UserRoleId(Resource):
    @jwt_required
    def get(self, id):
        userrole = UserRolesModel.by_id(id)

        userroles_part = UserRolesModel.to_json(userrole)

        useruserroles = UserUserRolesModel.by_user_role_id(userrole.id)
        userroles_part['users'] = []
        for uur in useruserroles:
            user = UserModel.by_id(uur.user_id)
            userroles_part['users'].append(UserModel.to_json(user))

        return userroles_part


class UserRoleName(Resource):
    @jwt_required
    def get(self, name):
        userrole = UserRolesModel.by_name(name)

        userroles_part = UserRolesModel.to_json(userrole)

        useruserroles = UserUserRolesModel.by_user_role_id(userrole.id)
        userroles_part['users'] = []
        for uur in useruserroles:
            user = UserModel.by_id(uur.user_id)
            userroles_part['users'].append(UserModel.to_json(user))

        return userroles_part


api.add_resource(UserRoles, '/v1/userroles')
api.add_resource(UserRoleId, '/v1/userrole/<int:id>')
api.add_resource(UserRoleName, '/v1/userrole/<string:name>')
