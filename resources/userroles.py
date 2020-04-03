from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import UserModel, UserRolesModel, UserUserRolesModel


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


api.add_resource(UserRoles, '/v1/userroles')
