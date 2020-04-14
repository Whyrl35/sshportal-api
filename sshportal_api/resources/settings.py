from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import SettingsModel
from flask_restful_swagger_2 import swagger


class Settings(Resource):
    @swagger.doc({
        'tags': ['setting'],
        'description': "Return list of settings",
        'responses': {
            '200': {
                'description': "A list of settings",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': []
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self):
        return [SettingsModel.to_json(x) for x in SettingsModel.return_all()]


class Setting(Resource):
    @swagger.doc({
        'tags': ['setting'],
        'description': "Return a setting that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a setting',
                'in': 'path',
                'schema': {
                    'type': 'integer',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The setting that match the ID",
                'content': {
                    'application/json': {
                        'examples': {}
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        return SettingsModel.to_json(SettingsModel.by_id(id))


api.add_resource(Settings, '/v1/settings')
api.add_resource(Setting, '/v1/setting/<int:id>')
