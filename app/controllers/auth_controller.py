from app.extensions import db
from app.models.user import User, Role
from app.utils.responses import success_response, error_response

def register_account(data):
    if not all([data.get("username"), data.get("email"), data.get("password"), data.get("role")]):
        return error_response("All fields are required", 400)

    if User.query.filter_by(email=data["email"]).first():
        return error_response("Email already exists", 409)

    if User.query.filter_by(username=data["username"]).first():
        return error_response("Username already exists", 409)

    role = Role.query.filter_by(name=data["role"]).first()
    if not role:
        return error_response("Invalid role", 400)

    user = User(username=data["username"], email=data["email"], password=data["password"], role=role)
    db.session.add(user)
    db.session.commit()
    return success_response("User registered successfully", {"username": user.username}, 201)

def login_account(data):
    user = User.query.filter_by(username=data.get("username")).first()
    if user and user.password == data.get("password"):
        return success_response("Login successful", {"username": user.username, "role": user.role.name}, 200)
    return error_response("Invalid credentials", 401)
