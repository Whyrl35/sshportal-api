from . import db


class SessionsModel(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True), index=True)
    stopped_at = db.Column(db.DateTime(timezone=True), index=True)
    status = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    host_id = db.Column(db.Integer)
    err_msg = db.Column(db.String(255))
    comment = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(session):
        if session is None:
            return {}
        return {
            'id': session.id,
            'created_at': session.created_at.isoformat() if session.created_at else None,
            'updated_at': session.updated_at.isoformat() if session.updated_at else None,
            'deleted_at': session.deleted_at.isoformat() if session.deleted_at else None,
            'stopped_at': session.stopped_at.isoformat() if session.deleted_at else None,
            'status': session.status,
            'user_id': session.user_id,
            'host_id': session.host_id,
            'err_msg': session.err_msg,
            'comment': session.comment,
        }

    @classmethod
    def by_id(cls, host_group_id):
        return cls.query.filter_by(id=host_group_id).first()

    @classmethod
    def return_all(cls):
        return cls.query.all()
