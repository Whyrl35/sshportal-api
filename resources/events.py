from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from run import api
from .models import EventsModel


class Events(Resource):
    @jwt_required
    def get(self):
        return [EventsModel.to_json(x) for x in EventsModel.return_all()]


api.add_resource(Events, '/v1/events')
