from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.inventory import Inventory
from app.models.product import Product
from app.models.user import User
from app.schemas.inventory_schema import InventorySchema
from app.utils.responses import success_response, error_response

inventory_bp = Blueprint("inventory", __name__)
inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

def is_admin():
    user = User.query.get(get_jwt_identity())
    return user and user.role.name == "Admin"

@inventory_bp.route("", methods=["POST"])
@jwt_required()
def add_inventory():
    if not is_admin():
        return error_response("Admin role required", 403)

    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not product_id or not quantity:
        return error_response("Product ID and quantity are required", 400)

    product = Product.query.get(product_id)
    if not product:
        return error_response("Product not found", 404)

    inventory = Inventory(product_id=product_id, quantity=quantity)
    db.session.add(inventory)
    db.session.commit()
    return success_response("Inventory added successfully", inventory_schema.dump(inventory), 201)

@inventory_bp.route("", methods=["GET"])
@jwt_required()
def list_inventory():
    inventories = Inventory.query.all()
    return success_response("Inventory retrieved", inventories_schema.dump(inventories))

@inventory_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_inventory(id):
    if not is_admin():
        return error_response("Admin role required", 403)

    inventory = Inventory.query.get(id)
    if not inventory:
        return error_response("Inventory record not found", 404)

    db.session.delete(inventory)
    db.session.commit()
    return success_response("Inventory deleted successfully", None, 200)
