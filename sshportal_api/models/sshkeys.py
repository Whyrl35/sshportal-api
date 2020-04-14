from . import db


class SshKeysModel(db.Model):
    __tablename__ = 'ssh_keys'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True), index=True)
    name = db.Column(db.String(255), unique=True)
    type = db.Column(db.String(255))
    length = db.Column(db.Integer)
    fingerprint = db.Column(db.String(255))
    priv_key = db.Column(db.String(10000))
    pub_key = db.Column(db.String(10000))
    comment = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(key):
        if key is None:
            return {}
        return {
            'id': key.id,
            'created_at': key.created_at.isoformat() if key.created_at else None,
            'updated_at': key.updated_at.isoformat() if key.updated_at else None,
            'deleted_at': key.deleted_at.isoformat() if key.deleted_at else None,
            'name': key.name,
            'type': key.type,
            'length': key.length,
            'fingerprint': key.fingerprint,
            'priv_key': key.priv_key,
            'pub_key': key.pub_key,
            'comment': key.comment,
        }

    @classmethod
    def by_id(cls, id):
        result = cls.query.filter_by(id=id)
        return result.first()

    @classmethod
    def by_ids(cls, ids):
        return cls.query.filter(cls.id.in_(ids))

    @classmethod
    def by_name(cls, name):
        result = cls.query.filter_by(name=name)
        return result.first()

    @classmethod
    def return_all(cls):
        return cls.query.all()
