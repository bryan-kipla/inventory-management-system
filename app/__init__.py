from flask import Flask
from app.extensions import db, migrate, ma
from flask_jwt_extended import JWTManager
from app.routes.auth_routes import auth_bp
from app.routes.category_routes import category_bp
from app.routes.product_routes import product_bp
from app.routes.supplier_routes import supplier_bp
from app.routes.inventory_routes import inventory_bp
from app.utils.error_handlers import register_error_handlers

jwt = JWTManager()  # initialize JWT

def create_app(config_class="instance.config.DevConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)   # attach JWT to app

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(category_bp, url_prefix="/categories")
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(supplier_bp, url_prefix="/suppliers")
    app.register_blueprint(inventory_bp, url_prefix="/inventory")

    # Error handlers
    register_error_handlers(app)

    return app
