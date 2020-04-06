from . import db
from sqlalchemy import PrimaryKeyConstraint


class UserGroupsModel(db.Model):
    __tablename__ = 'user_groups'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    name = db.Column(db.String(255), unique=True)
    comment = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(user_group):
        if user_group is None:
            return {}
        return {
            'id': user_group.id,
            'created_at': user_group.created_at.isoformat() if user_group.created_at else None,
            'updated_at': user_group.updated_at.isoformat() if user_group.updated_at else None,
            'deleted_at': user_group.deleted_at.isoformat() if user_group.deleted_at else None,
            'name': user_group.name,
            'comment': user_group.comment,
        }

    @classmethod
    def by_name(cls, user_group_name):
        return cls.query.filter_by(name=user_group_name).first()

    @classmethod
    def by_id(cls, user_group_id):
        return cls.query.filter_by(id=user_group_id).first()

    @classmethod
    def by_ids(cls, user_group_ids):
        return cls.query.filter(cls.id.in_(user_group_ids))

    @classmethod
    def return_all(cls):
        return cls.query.all()


class UserUserGroupsModel(db.Model):
    __tablename__ = 'user_user_groups'

    user_id = db.Column(db.Integer)
    user_group_id = db.Column(db.Integer)
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'user_group_id'),
        {},
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def by_user_group_id(cls, user_group_id):
        return cls.query.filter_by(user_group_id=user_group_id)

    @classmethod
    def by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id)
