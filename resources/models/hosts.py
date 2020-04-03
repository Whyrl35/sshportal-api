from . import db
import paramiko


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
        if host is None:
            return {}

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
    def by_id(cls, id):
        result = cls.query.filter_by(id=id)
        return result.first()

    @classmethod
    def by_ids(cls, host_ids):
        return cls.query.filter(cls.id.in_(host_ids))

    @classmethod
    def by_name(cls, name):
        result = cls.query.filter_by(name=name)
        return result.first()

    @classmethod
    def by_ssh_key_id(cls, id):
        return cls.query.filter_by(ssh_key_id=id)

    @classmethod
    def return_all(cls):
        return cls.query.all()
