from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models.user import User
from app.utils.responses import error_response

def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user = User.query.get(get_jwt_identity())
            if not user or user.role.name != required_role:
                return error_response(f"{required_role} role required", 403)
            return fn(*args, **kwargs)
        return wrapper
    return decorator
