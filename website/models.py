from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    admin_first = db.Column(db.String())
    admin_last = db.Column(db.String())
    member = db.relationship('Member')


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_first = db.Column(db.String())
    member_last = db.Column(db.String())
    member_email = db.Column(db.String(), unique=True)
    member_address = db.Column(db.String())
    category = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
