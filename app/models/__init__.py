from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User  # noqa: F401
from .booking import Booking  # noqa: F401
from .role import Role  # noqa: F401
from .rewards import RewardTransaction  # noqa: F401

__all__ = ['db', 'User', 'Booking', 'Role', 'RewardTransaction']