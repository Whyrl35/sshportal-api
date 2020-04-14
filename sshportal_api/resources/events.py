from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import EventsModel
from flask_restful_swagger_3 import swagger


class Events(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['event'],
        'description': "Return list of events",
        'responses': {
            '200': {
                'description': "A list of events",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': [
                                {
                                    "id": 1,
                                    "created_at": "2019-11-13T16:08:45.370956",
                                    "updated_at": "2019-11-13T16:08:45.370956",
                                    "deleted_at": None,
                                    "author_id": 0,
                                    "domain": "system",
                                    "action": "migrated",
                                    "entity": "",
                                    "args": None
                                }
                            ]
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self):
        return [EventsModel.to_json(x) for x in EventsModel.return_all()]


class Event(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['event'],
        'description': "Return an event that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of an event',
                'in': 'path',
                'schema': {
                    'type': 'integer',
                }
            }
        ],
        'responses': {
            '200': {
                'description': "The event that match the ID",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "id": 1,
                                "created_at": "2019-11-13T16:08:45.370956",
                                "updated_at": "2019-11-13T16:08:45.370956",
                                "deleted_at": None,
                                "author_id": 0,
                                "domain": "system",
                                "action": "migrated",
                                "entity": "",
                                "args": None
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        return EventsModel.to_json(EventsModel.by_id(id))


api.add_resource(Events, '/v1/events')
api.add_resource(Event, '/v1/event/<int:id>')
