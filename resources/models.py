from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import exc, PrimaryKeyConstraint, MetaData
from run import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import paramiko

# FIXME: https://github.com/blakev/Flask-WhooshAlchemy3
# need to index movie on title, seen, is_series

if app.config['DATABASE']['type'] == 'sqlite':
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE']['sqlite']['uri']
elif app.config['DATABASE']['type'] == 'mysql':
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{username}:{password}@{host}/{database}".format(
        username=app.config['DATABASE']['mysql']['user'],
        password=app.config['DATABASE']['mysql']['password'],
        host=app.config['DATABASE']['mysql']['host'],
        database=app.config['DATABASE']['mysql']['database'],
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

metadata = MetaData(
  naming_convention={
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'idx_%(table_name)s_%(column_0_name)s',
    'uq': 'uix_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    }
)

db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


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


class HostGroupsModel(db.Model):
    __tablename__ = 'host_groups'

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
    def to_json(host_group):
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


class HostsModel(db.Model):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    name = db.Column(db.String(255), unique=True)
    addr = db.Column(db.String(255))
    user = db.Column(db.String(255))
    password = db.Column(db.String(255))
    ssh_key_id = db.Column(db.Integer(), index=True)
    fingerprint = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    host_key = db.Column(db.LargeBinary(255))
    url = db.Column(db.String(255))
    hop_id = db.Column(db.Integer())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(host):
        key = paramiko.RSAKey(data=host.host_key) if host.host_key else None
        base64_key = key.get_base64() if key else None
        return {
            'id': host.id,
            'created_at': host.created_at.isoformat() if host.created_at else None,
            'updated_at': host.updated_at.isoformat() if host.updated_at else None,
            'deleted_at': host.deleted_at.isoformat() if host.deleted_at else None,
            'name': host.name,
            'addr': host.addr,
            'user': host.user,
            'password': host.password,
            'ssh_key_id': host.ssh_key_id,
            'fingerprint': host.fingerprint,
            'comment': host.comment,
            'host_key': base64_key,
            'url': host.url,
            'hop_ip': host.hop_id,
        }

    @classmethod
    def by_id(cls, host_id):
        result = cls.query.filter_by(id=host_id)
        return result.first()

    @classmethod
    def by_ids(cls, host_ids):
        return cls.query.filter(cls.id.in_(host_ids))

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


class EventsModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
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
    def return_all(cls):
        return cls.query.all()


class SessionsModel(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    stopped_at = db.Column(db.DateTime(), index=True)
    status = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    host_id = db.Column(db.Integer)
    err_msg = db.Column(db.String(255))
    comment = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class SettingsModel(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
    name = db.Column(db.String(255), unique=True)
    value = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class SshKeysModel(db.Model):
    __tablename__ = 'ssh_keys'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime(), index=True)
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

    @staticmethod
    def to_json(user):
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
