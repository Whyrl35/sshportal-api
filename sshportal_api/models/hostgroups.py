from . import db
from sqlalchemy import PrimaryKeyConstraint


class HostGroupsModel(db.Model):
    __tablename__ = 'host_groups'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True), index=True)
    name = db.Column(db.String(255), unique=True)
    comment = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(host_group):
        if host_group is None:
            return {}
        return {
            'id': host_group.id,
            'created_at': host_group.created_at.isoformat() if host_group.created_at else None,
            'updated_at': host_group.updated_at.isoformat() if host_group.updated_at else None,
            'deleted_at': host_group.deleted_at.isoformat() if host_group.deleted_at else None,
            'name': host_group.name,
            'comment': host_group.comment,
        }

    @classmethod
    def by_name(cls, host_group_name):
        return cls.query.filter_by(name=host_group_name).one()

    @classmethod
    def by_id(cls, host_group_id):
        return cls.query.filter_by(id=host_group_id).one()

    @classmethod
    def by_ids(cls, host_group_ids):
        return cls.query.filter(cls.id.in_(host_group_ids))

    @classmethod
    def return_all(cls):
        return cls.query.all()


class HostHostGroupsModel(db.Model):
    __tablename__ = 'host_host_groups'

    host_id = db.Column(db.Integer)
    host_group_id = db.Column(db.Integer)
    __table_args__ = (
        PrimaryKeyConstraint('host_id', 'host_group_id'),
        {},
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def by_host_id(cls, host_id):
        return cls.query.filter_by(host_id=host_id).first()

    @classmethod
    def by_host_group_id(cls, host_group_id):
        return cls.query.filter_by(host_group_id=host_group_id)
