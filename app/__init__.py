from flask import Flask
from app.routes.auth_routes import auth_bp

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key_here"

    # Register authentication blueprint
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
