# Role constants
class Role:
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

# Plain User class (no SQLAlchemy)
class User:
    def __init__(self, username, email, password, role=Role.USER):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
