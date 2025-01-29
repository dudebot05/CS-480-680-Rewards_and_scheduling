from functools import wraps
from flask import abort
from flask_login import current_user
from ..models.permission import Permission
from .. import login_manager
from ..models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)