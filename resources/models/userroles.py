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
