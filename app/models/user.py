from flask import current_app
from .. import db
from .role import Role
from .booking import Booking
from .rewards import RewardTransaction
from .permission import Permission
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    reward_points = db.Column(db.Integer, default=0)
    bookings = db.relationship('Booking', backref='user', lazy='dynamic')
    reward_transactions = db.relationship('RewardTransaction', backref='user', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions
    
    def is_client(self):
        return self.can(Permission.SET_REWARDS)
    
    def is_administrator(self):
        return self.can(Permission.ADMINISTER)