from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import UserKeysModel, UserModel


class UserKeys(Resource):
    @jwt_required
    def get(self):
        userkeys_json = []
        userkeys = UserKeysModel.return_all()

        for userkey in userkeys:
            userkeys_part = UserKeysModel.to_json(userkey)
            userkeys_json.append(userkeys_part)

            user = UserModel.by_id(userkey.user_id)
            userkeys_part['user'] = UserModel.to_json(user)

            userkeys_json.append(userkeys_part)

        return userkeys_json


api.add_resource(UserKeys, '/v1/userkeys')
