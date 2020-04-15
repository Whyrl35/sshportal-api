from flask_restful import Resource  # , reqparse
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import AclsModel, UserModel, HostsModel, SshKeysModel, SessionsModel, EventsModel
from flask_restful_swagger_3 import swagger


class Statistics(Resource):
    @swagger.doc({
        'security': [{'bearerAuth': []}],
        'tags': ['statistics'],
        'description': "Return statistics over the differents objects",
        'responses': {
            '200': {
                'description': "A list of statistics on the different objects",
                'content': {
                    'application/json': {
                        'examples': {
                            'application/json': {
                                "users": {
                                    "count": 1
                                },
                                "keys": {
                                    "count": 3
                                },
                                "hosts": {
                                    "count": 8
                                },
                                "acls": {
                                    "count": 3
                                },
                                "sessions": {
                                    "count": 415
                                },
                                "events": {
                                    "count": 803
                                }
                            }
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self):
        users = UserModel.return_all()
        keys = SshKeysModel.return_all()
        hosts = HostsModel.return_all()
        acls = AclsModel.return_all()
        sessions = SessionsModel.return_all()
        events = EventsModel.return_all()

        return {
            'users': {
                'count': len(users)
            },
            'keys': {
                'count': len(keys)
            },
            'hosts': {
                'count': len(hosts)
            },
            'acls': {
                'count': len(acls)
            },
            'sessions': {
                'count': len(sessions)
            },
            'events': {
                'count': len(events)
            }
        }


api.add_resource(Statistics, '/v1/statistics')
