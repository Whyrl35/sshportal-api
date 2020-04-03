from . import db
from sqlalchemy import PrimaryKeyConstraint


class UserRolesModel(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    name = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(user_role):
        return {
            'id': user_role.id,
            'created_at': user_role.created_at.isoformat() if user_role.created_at else None,
            'updated_at': user_role.updated_at.isoformat() if user_role.updated_at else None,
            'deleted_at': user_role.deleted_at.isoformat() if user_role.deleted_at else None,
            'name': user_role.name,
        }

    @classmethod
    def return_all(cls):
        return cls.query.all()


class UserUserRolesModel(db.Model):
    __tablename__ = 'user_user_roles'

    user_role_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    __table_args__ = (
        PrimaryKeyConstraint('user_role_id', 'user_id'),
        {},
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def by_user_role_id(cls, user_role_id):
        return cls.query.filter_by(user_role_id=user_role_id)

    @classmethod
    def by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
