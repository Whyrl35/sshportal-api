from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import SettingsModel


class Settings(Resource):
    @jwt_required
    def get(self):
        return [SettingsModel.to_json(x) for x in SettingsModel.return_all()]


api.add_resource(Settings, '/v1/settings')
