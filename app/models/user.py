from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize SQLAlchemy instance

class Role:
    MANAGER = "manager"  # Role constant for managers
    USER = "user"        # Role constant for regular users

class User(db.Model):
    __tablename__ = "users"  # Table name in SQLite database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    email = db.Column(db.String(120), unique=True, nullable=False)    # Unique email
    password = db.Column(db.String(200), nullable=False)              # Plain text password
    role = db.Column(db.String(20), nullable=False, default=Role.USER) # User role

