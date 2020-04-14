from . import db
import json


class EventsModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True), index=True)
    author_id = db.Column(db.String(255))
    domain = db.Column(db.String(255))
    action = db.Column(db.String(255))
    entity = db.Column(db.String(255))
    args = db.Column(db.LargeBinary(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(event):
        if event is None:
            return {}
        return {
            'id': event.id,
            'created_at': event.created_at.isoformat() if event.created_at else None,
            'updated_at': event.updated_at.isoformat() if event.updated_at else None,
            'deleted_at': event.deleted_at.isoformat() if event.deleted_at else None,
            'author_id': event.author_id,
            'domain': event.domain,
            'action': event.action,
            'entity': event.entity,
            'args': json.loads(event.args.decode('UTF-8')) if event.args else None,
        }

    @classmethod
    def by_id(cls, host_group_id):
        return cls.query.filter_by(id=host_group_id).one()

    @classmethod
    def return_all(cls):
        return cls.query.all()
