from flask import Blueprint, request, jsonify
from app.controllers import auth_controller

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response, status = auth_controller.register_account(data)
    return jsonify(response), status

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response, status = auth_controller.login_account(data)
    return jsonify(response), status
