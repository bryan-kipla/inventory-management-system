from flask import Flask
from app.database import db
from app.routes.auth_routes import auth_bp

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key_here"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Bind db to app
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register authentication blueprint
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
