from flask import Blueprint, request, jsonify
from app.controllers import auth_controller

# Define blueprint for authentication routes
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register/manager", methods=["POST"])
def register_manager():
    # Endpoint to register a manager
    data = request.get_json()
    response, status = auth_controller.register_manager(data)
    return jsonify(response), status

@auth_bp.route("/register/user", methods=["POST"])
def register_user():
    # Endpoint to register a regular user
    data = request.get_json()
    response, status = auth_controller.register_user(data)
    return jsonify(response), status

@auth_bp.route("/login/manager", methods=["POST"])
def login_manager():
    # Endpoint for manager login
    data = request.get_json()
    response, status = auth_controller.login_manager(data)
    return jsonify(response), status

@auth_bp.route("/login/user", methods=["POST"])
def login_user():
    # Endpoint for user login
    data = request.get_json()
    response, status = auth_controller.login_user(data)
    return jsonify(response), status
