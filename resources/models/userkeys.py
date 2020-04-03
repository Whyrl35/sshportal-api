from . import db


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
