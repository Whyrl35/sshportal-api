from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import SettingsModel


class Settings(Resource):
    @jwt_required
    def get(self):
        return [SettingsModel.to_json(x) for x in SettingsModel.return_all()]


class Setting(Resource):
    @jwt_required
    def get(self, id):
        return SettingsModel.to_json(SettingsModel.by_id(id))


api.add_resource(Settings, '/v1/settings')
api.add_resource(Setting, '/v1/setting/<int:id>')
