def check_role(user, required_role):
    """
    Check if a user has the required role.
    Example: check_role(current_user, "admin")
    """
    return user.role.name == required_role
