from . import db
from sqlalchemy import PrimaryKeyConstraint


class AclsModel(db.Model):
    __tablename__ = 'acls'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    host_pattern = db.Column(db.String(255))
    action = db.Column(db.String(255))
    weight = db.Column(db.String(255))
    comment = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(acl):
        if acl is None:
            return {}
        return {
            'id': acl.id,
            'created_at': acl.created_at.isoformat() if acl.created_at else None,
            'updated_at': acl.updated_at.isoformat() if acl.updated_at else None,
            'deleted_at': acl.deleted_at.isoformat() if acl.deleted_at else None,
            'host_pattern': acl.host_pattern,
            'action': acl.action,
            'weight': acl.weight,
            'comment': acl.comment,
        }

    @classmethod
    def by_id(cls, acl_id):
        return cls.query.filter_by(id=acl_id).one()

    @classmethod
    def by_ids(cls, acl_ids):
        return cls.query.filter(cls.id.in_(acl_ids))

    @classmethod
    def return_all(cls):
        return cls.query.all()


class HostGroupAclsModel(db.Model):
    __tablename__ = 'host_group_acls'

    host_group_id = db.Column(db.Integer)
    acl_id = db.Column(db.Integer)
    __table_args__ = (
        PrimaryKeyConstraint('host_group_id', 'acl_id'),
        {},
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def by_acl_id(cls, acl_id):
        return cls.query.filter_by(acl_id=acl_id).first()

    @classmethod
    def by_host_group_id(cls, host_group_id):
        return cls.query.filter_by(host_group_id=host_group_id)


class UserGroupAclModel(db.Model):
    __tablename__ = 'user_group_acls'

    user_group_id = db.Column(db.Integer)
    acl_id = db.Column(db.Integer)
    __table_args__ = (
        PrimaryKeyConstraint('user_group_id', 'acl_id'),
        {},
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def by_acl_id(cls, acl_id):
        return cls.query.filter_by(acl_id=acl_id).first()

    @classmethod
    def by_user_group_id(cls, user_group_id):
        return cls.query.filter_by(user_group_id=user_group_id)
