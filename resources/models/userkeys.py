from . import db
import paramiko


class UserKeysModel(db.Model):
    __tablename__ = 'user_keys'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    key = db.Column(db.LargeBinary(255))
    user_id = db.Column(db.Integer)
    comment = db.Column(db.String(255))
    authorized_key = db.Column(db.String(10000))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(user_key):
        key = paramiko.RSAKey(data=user_key.key) if user_key.key else None
        base64_key = key.get_base64() if key else None

        return {
            'id': user_key.id,
            'created_at': user_key.created_at.isoformat() if user_key.created_at else None,
            'updated_at': user_key.updated_at.isoformat() if user_key.updated_at else None,
            'deleted_at': user_key.deleted_at.isoformat() if user_key.deleted_at else None,
            'key': base64_key,
            'user_id': user_key.user_id,
            'comment': user_key.comment,
            'authorized_key': user_key.authorized_key,
        }

    @classmethod
    def return_all(cls):
        return cls.query.all()
