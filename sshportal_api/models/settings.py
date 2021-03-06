from . import db


class SettingsModel(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True), index=True)
    name = db.Column(db.String(255), unique=True)
    value = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(item):
        if item is None:
            return {}
        return {
            'id': item.id,
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'updated_at': item.updated_at.isoformat() if item.updated_at else None,
            'deleted_at': item.deleted_at.isoformat() if item.deleted_at else None,
            'name': item.name,
            'value': item.value,
        }

    @classmethod
    def by_id(cls, host_group_id):
        return cls.query.filter_by(id=host_group_id).first()

    @classmethod
    def return_all(cls):
        return cls.query.all()
