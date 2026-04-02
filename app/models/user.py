from app.database import db  # Import the shared db instance

#role constants
class Role:
    ADMIN = "admin"      
    MANAGER = "manager"  
    USER = "user"        

class User(db.Model):
    __tablename__ = "users"  # Table name in SQLite database

    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80), unique=True, nullable=False)  
    email = db.Column(db.String(120), unique=True, nullable=False)    
    password = db.Column(db.String(200), nullable=False)              
    role = db.Column(db.String(20), nullable=False, default=Role.USER) 
