from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import UserKeysModel, UserModel


class UserKeys(Resource):
    @jwt_required
    def get(self):
        userkeys_json = []
        userkeys = UserKeysModel.return_all()

        for userkey in userkeys:
            userkeys_part = UserKeysModel.to_json(userkey)

            user = UserModel.by_id(userkey.user_id)
            userkeys_part['user'] = UserModel.to_json(user)

            userkeys_json.append(userkeys_part)

        return userkeys_json


class UserKey(Resource):
    @jwt_required
    def get(self, id):
        userkey = UserKeysModel.by_id(id)

        userkeys_part = UserKeysModel.to_json(userkey)

        user = UserModel.by_id(userkey.user_id)
        userkeys_part['user'] = UserModel.to_json(user)

        return userkeys_part


api.add_resource(UserKeys, '/v1/userkeys')
api.add_resource(UserKey, '/v1/userkey/<int:id>')
