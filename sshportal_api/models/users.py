from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import exc
from . import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    is_admin = db.Column(db.Boolean())
    email = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    invite_token = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def to_json(user):
        if user is None:
            return {}
        return {
            'id': user.id,
            'name': user.name,
            'password': user.password,
            'created_at': user.created_at.isoformat() if user.created_at else None,
            'updated_at': user.updated_at.isoformat() if user.updated_at else None,
            'deleted_at': user.deleted_at.isoformat() if user.deleted_at else None,
            'is_admin': user.is_admin,
            'email': user.email,
            'comment': user.comment,
            'invite_token': user.invite_token,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def by_id(cls, id):
        result = cls.query.filter_by(id=id)
        return result.first()

    @classmethod
    def by_ids(cls, ids):
        return cls.query.filter(cls.id.in_(ids))

    @classmethod
    def return_all(cls):
        return {'users': list(map(lambda x: cls.to_json(x), cls.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except exc.SQLAlchemyError:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, phash):
        return sha256.verify(password, phash)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
