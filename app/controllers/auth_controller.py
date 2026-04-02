from app.models.user import db, User, Role

# Validation Layer
def validate_payload(data, required_fields):
    """Check that all required fields exist and are non-empty."""
    errors = []
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{field} is required")

    # Password must be at least 6 characters
    if "password" in required_fields and data.get("password") and len(data["password"]) < 6:
        errors.append("Password must be at least 6 characters long")

    # Role must be provided and valid
    if "role" in required_fields:
        role_value = data.get("role")
        if not role_value:
            errors.append("Role is required")
        elif role_value.lower() not in ["user", "manager", "admin"]:
            errors.append("Role must be either 'user', 'manager', or 'admin'")

    return errors


# Registration
def register_account(data):
    errors = validate_payload(data, ["username", "email", "password", "role"])
    if errors:
        return {"error": errors}, 400

    # Check if email already exists
    if User.query.filter_by(email=data["email"]).first():
        return {"error": f"{data['role'].capitalize()} with this email already exists"}, 409

    # Check if username already exists
    if User.query.filter_by(username=data["username"]).first():
        return {"error": f"Username '{data['username']}' is already taken"}, 409

    # Map role string to Role enum
    role_map = {"user": Role.USER, "manager": Role.MANAGER, "admin": Role.ADMIN}
    role_enum = role_map.get(data["role"].lower())

    # Create new account
    user = User(username=data["username"], email=data["email"],
                password=data["password"], role=role_enum)
    db.session.add(user)
    db.session.commit()
    return {"message": f"{data['role'].capitalize()} registered successfully"}, 201


# Login
def login_account(data):
    errors = validate_payload(data, ["username", "password", "role"])
    if errors:
        return {"error": errors}, 400

    # Map role string to Role enum
    role_map = {"user": Role.USER, "manager": Role.MANAGER, "admin": Role.ADMIN}
    role_enum = role_map.get(data["role"].lower())

    # Authenticate login by username + password + role
    user = User.query.filter_by(username=data["username"], role=role_enum).first()
    if user and user.password == data["password"]:
        return {"message": f"{data['role'].capitalize()} login successful",
                "role": user.role, "email": user.email}, 200
    return {"error": f"Invalid {data['role']} credentials"}, 401
