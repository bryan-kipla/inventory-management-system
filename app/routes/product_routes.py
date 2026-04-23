from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.product import Product
from app.models.category import Category
from app.models.user import User
from app.schemas.product_schema import ProductSchema
from app.utils.responses import success_response, error_response

product_bp = Blueprint("products", __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def is_admin():
    user = User.query.get(get_jwt_identity())
    return user and user.role.name == "Admin"

@product_bp.route("", methods=["POST"])
@jwt_required()
def create_product():
    if not is_admin():
        return error_response("Admin role required", 403)

    data = request.get_json()
    name = data.get("name")
    category_id = data.get("category_id")
    price = data.get("price")

    if not name or not category_id or not price:
        return error_response("Name, category_id, and price are required", 400)

    category = Category.query.get(category_id)
    if not category:
        return error_response("Invalid category_id", 404)

    product = Product(name=name, category_id=category_id, price=price)
    db.session.add(product)
    db.session.commit()
    return success_response("Product created successfully", product_schema.dump(product), 201)

@product_bp.route("", methods=["GET"])
@jwt_required()
def list_products():
    products = Product.query.all()
    return success_response("Products retrieved", products_schema.dump(products))

@product_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    if not is_admin():
        return error_response("Admin role required", 403)

    product = Product.query.get(id)
    if not product:
        return error_response("Product not found", 404)

    db.session.delete(product)
    db.session.commit()
    return success_response("Product deleted successfully", None, 200)
