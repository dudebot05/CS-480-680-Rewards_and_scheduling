from flask import current_app
from . import db
from .role import Role  # noqa: F401
from .booking import Booking  # noqa: F401
from .rewards import RewardTransaction  # noqa: F401
from .permission import Permission  # noqa: F401
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from typing import Optional

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id: int = db.Column(db.Integer, primary_key = True)
    email: str = db.Column(db.String(64), unique=True, index=True)
    username: str = db.Column(db.String(64), unique=True, index=True)
    password_hash: str = db.Column(db.String(128))
    is_active: bool = db.Column(db.Boolean, default=True)
    reward_points: int = db.Column(db.Integer, default=0)
    bookings = db.relationship('Booking', backref='user', lazy='dynamic')
    reward_transactions = db.relationship('RewardTransaction', backref='user', lazy='dynamic')
    role_id: int = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self) -> str:
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    def __init__(self, **kwargs) -> None:
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions: int) -> bool:
        return self.role is not None and (self.role.permissions & permissions) == permissions
    
    def is_client(self) -> bool:
        return self.can(Permission.SET_REWARDS)
    
    def is_administrator(self) -> bool:
        return self.can(Permission.ADMINISTER)
    
    def generate_password_reset_token(self) -> str:
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(self.email, salt=self.password_hash)
    
    @staticmethod
    def validate_reset_password_token(token: str, user_id: int) -> Optional['User']:
        user = db.session.get(User, user_id)

        if user is None:
            return None
        
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            token_user_email = serializer.loads(
                token, 
                max_age=current_app.config['RESET_PASS_TOKEN_MAX_AGE'], 
                salt=user.password_hash
            )
        except(BadSignature, SignatureExpired):
            return None
        
        if token_user_email != user.email:
            return None
        
        return user