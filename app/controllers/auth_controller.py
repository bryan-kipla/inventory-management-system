
users = []
roles = ["user", "manager", "admin"]

# Validation Layer
def validate_payload(data, required_fields):
    errors = []
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{field} is required")

    if "password" in required_fields and data.get("password") and len(data["password"]) < 6:
        errors.append("Password must be at least 6 characters long")

    if "role" in required_fields:
        role_value = data.get("role")
        if not role_value:
            errors.append("Role is required")
        elif role_value.lower() not in roles:
            errors.append("Role must be either 'user', 'manager', or 'admin'")

    return errors


# Registration
def register_account(data):
    errors = validate_payload(data, ["username", "email", "password", "role"])
    if errors:
        return {"error": errors}, 400

    # Check duplicates
    for user in users:
        if user["email"] == data["email"]:
            return {"error": f"{data['role'].capitalize()} with this email already exists"}, 409
        if user["username"] == data["username"]:
            return {"error": f"Username '{data['username']}' is already taken"}, 409

    # Save user in memory
    new_user = {
        "username": data["username"],
        "email": data["email"],
        "password": data["password"],  # plain text for demo
        "role": data["role"].lower()
    }
    users.append(new_user)
    return {"message": f"{data['role'].capitalize()} registered successfully"}, 201


# Login
def login_account(data):
    errors = validate_payload(data, ["username", "password", "role"])
    if errors:
        return {"error": errors}, 400

    for user in users:
        if (user["username"] == data["username"] and
            user["password"] == data["password"] and
            user["role"] == data["role"].lower()):
            return {"message": f"{data['role'].capitalize()} login successful",
                    "role": user["role"], "email": user["email"]}, 200

    return {"error": f"Invalid {data['role']} credentials"}, 401
