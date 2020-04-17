from flask_restful import Resource
from sshportal_api import api


class Ping(Resource):
    def get(self):
        return {"message": "Pong!"}


api.add_resource(Ping, '/v1/ping')
