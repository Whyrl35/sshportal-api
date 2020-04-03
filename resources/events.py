from flask_restful import Resource
from flask_jwt_extended import jwt_required
from run import api
from .models import EventsModel


class Events(Resource):
    @jwt_required
    def get(self):
        return [EventsModel.to_json(x) for x in EventsModel.return_all()]


class Event(Resource):
    @jwt_required
    def get(self, id):
        return EventsModel.to_json(EventsModel.by_id(id))


api.add_resource(Events, '/v1/events')
api.add_resource(Event, '/v1/event/<int:id>')
