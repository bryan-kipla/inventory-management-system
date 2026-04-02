from app.models.user import db, User, Role

def register_manager(data):
    # Create a new manager user with email
    user = User(username=data["username"], email=data["email"], password=data["password"], role=Role.MANAGER)
    db.session.add(user)
    db.session.commit()
    return {"message": "Manager registered successfully"}, 201

def register_user(data):
    # Create a new regular user with email
    user = User(username=data["username"], email=data["email"], password=data["password"], role=Role.USER)
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully"}, 201

def login_manager(data):
    # Authenticate manager login by username + password
    user = User.query.filter_by(username=data["username"], role=Role.MANAGER).first()
    if user and user.password == data["password"]:
        return {"message": "Manager login successful", "role": user.role, "email": user.email}, 200
    return {"error": "Invalid manager credentials"}, 401

def login_user(data):
    # Authenticate user login by username + password
    user = User.query.filter_by(username=data["username"], role=Role.USER).first()
    if user and user.password == data["password"]:
        return {"message": "User login successful", "role": user.role, "email": user.email}, 200
    return {"error": "Invalid user credentials"}, 401
