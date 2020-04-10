from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import SessionsModel, HostsModel, UserModel
from flask_restful_swagger_2 import swagger


class Sessions(Resource):
    @swagger.doc({
        'tags': ['session'],
        'description': "Return list of sessions",
        'responses': {
            '200': {
                'description': "A list of sessions",
                'examples': {
                    'application/json': [
                        {
                            "id": 1,
                            "created_at": "2019-11-13T16:42:16.969253",
                            "updated_at": "2019-11-13T16:42:17.397949",
                            "deleted_at": None,
                            "stopped_at": None,
                            "status": "closed",
                            "user_id": 1,
                            "host_id": 1,
                            "err_msg": "ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain",   # noqa
                            "comment": "",
                            "host": {
                                "id": 1,
                                "created_at": "2019-11-13T16:35:48.602836",
                                "updated_at": "2019-11-13T16:42:17.189908",
                                "deleted_at": None,
                                "name": "test",
                                "addr": "",
                                "user": "",
                                "password": "",
                                "ssh_key_id": 1,
                                "fingerprint": None,
                                "comment": "",
                                "host_key": "AAAAB3......+N",
                                "url": "ssh://admin@test.local",
                                "hop_ip": 0
                            },
                            "user": {
                                "id": 1,
                                "name": "admin",
                                "password": None,
                                "created_at": "2019-11-13T16:08:45.490830",
                                "updated_at": "2019-11-13T16:39:21.114928",
                                "deleted_at": None,
                                "is_admin": None,
                                "email": "admin@localhost",
                                "comment": "created by sshportal",
                                "invite_token": "1234567899"
                            }
                        }
                    ]
                }
            }
        }
    })
    @jwt_required
    def get(self):
        sessions_json = []
        sessions = SessionsModel.return_all()

        for session in sessions:
            sessions_part = SessionsModel.to_json(session)

            host = HostsModel.by_id(session.host_id)
            sessions_part['host'] = HostsModel.to_json(host) if host else None

            user = UserModel.by_id(session.user_id)
            sessions_part['user'] = UserModel.to_json(user) if user else None

            sessions_json.append(sessions_part)

        return sessions_json


class Session(Resource):
    @swagger.doc({
        'tags': ['session'],
        'description': "Return a session that match the given ID",
        'parameters': [
            {
                'name': 'id',
                'description': 'the id of a session',
                'in': 'path',
                'type': 'integer',
            }
        ],
        'responses': {
            '200': {
                'description': "The session that match the ID",
                # 'schema': ,
                'examples': {
                    'application/json': {
                        "id": 1,
                        "created_at": "2019-11-13T16:42:16.969253",
                        "updated_at": "2019-11-13T16:42:17.397949",
                        "deleted_at": None,
                        "stopped_at": None,
                        "status": "closed",
                        "user_id": 1,
                        "host_id": 1,
                        "err_msg": "ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain",   # noqa
                        "comment": "",
                        "host": {
                            "id": 1,
                            "created_at": "2019-11-13T16:35:48.602836",
                            "updated_at": "2019-11-13T16:42:17.189908",
                            "deleted_at": None,
                            "name": "test",
                            "addr": "",
                            "user": "",
                            "password": "",
                            "ssh_key_id": 1,
                            "fingerprint": None,
                            "comment": "",
                            "host_key": "AAAAB3......+N",
                            "url": "ssh://admin@test.local",
                            "hop_ip": 0
                        },
                        "user": {
                            "id": 1,
                            "name": "admin",
                            "password": None,
                            "created_at": "2019-11-13T16:08:45.490830",
                            "updated_at": "2019-11-13T16:39:21.114928",
                            "deleted_at": None,
                            "is_admin": None,
                            "email": "admin@localhost",
                            "comment": "created by sshportal",
                            "invite_token": "1234567899"
                        }
                    }
                }
            }
        }
    })
    @jwt_required
    def get(self, id):
        session = SessionsModel.by_id(id)

        sessions_part = SessionsModel.to_json(session)

        host = HostsModel.by_id(session.host_id)
        sessions_part['host'] = HostsModel.to_json(host) if host else None

        user = UserModel.by_id(session.user_id)
        sessions_part['user'] = UserModel.to_json(user) if user else None

        return sessions_part


api.add_resource(Sessions, '/v1/sessions')
api.add_resource(Session, '/v1/session/<int:id>')
