from flask import Blueprint

main = Blueprint('main', __name__)

from . import dashboard
from . import booking

__all__ = ['main']