from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.category import Category
from app.models.user import User
from app.schemas.category_schema import CategorySchema
from app.utils.responses import success_response, error_response

category_bp = Blueprint("categories", __name__)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

def is_admin():
    user = User.query.get(get_jwt_identity())
    return user and user.role.name == "Admin"

@category_bp.route("", methods=["POST"])
@jwt_required()
def create_category():
    if not is_admin():
        return error_response("Admin role required", 403)

    data = request.get_json()
    if not data.get("name"):
        return error_response("Category name is required", 400)

    if Category.query.filter_by(name=data["name"]).first():
        return error_response("Category already exists", 409)

    category = Category(name=data["name"])
    db.session.add(category)
    db.session.commit()
    return success_response("Category created successfully", category_schema.dump(category), 201)

@category_bp.route("", methods=["GET"])
@jwt_required()
def list_categories():
    categories = Category.query.all()
    return success_response("Categories retrieved", categories_schema.dump(categories))

@category_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_category(id):
    if not is_admin():
        return error_response("Admin role required", 403)

    category = Category.query.get(id)
    if not category:
        return error_response("Category not found", 404)

    db.session.delete(category)
    db.session.commit()
    return success_response("Category deleted successfully", None, 200)
