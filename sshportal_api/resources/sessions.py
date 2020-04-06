from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sshportal_api import api
from sshportal_api.models import SessionsModel, HostsModel, UserModel


class Sessions(Resource):
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