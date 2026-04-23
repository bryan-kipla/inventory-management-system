from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.supplier import Supplier
from app.models.user import User
from app.schemas.supplier_schema import SupplierSchema
from app.utils.responses import success_response, error_response

supplier_bp = Blueprint("suppliers", __name__)
supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)

def is_admin():
    user = User.query.get(get_jwt_identity())
    return user and user.role.name == "Admin"

@supplier_bp.route("", methods=["POST"])
@jwt_required()
def create_supplier():
    if not is_admin():
        return error_response("Admin role required", 403)

    data = request.get_json()
    name = data.get("name")
    email = data.get("contact_email")
    phone = data.get("contact_phone")

    if not name:
        return error_response("Supplier name is required", 400)

    if Supplier.query.filter_by(name=name).first():
        return error_response("Supplier already exists", 409)

    supplier = Supplier(name=name, contact_email=email, contact_phone=phone)
    db.session.add(supplier)
    db.session.commit()
    return success_response("Supplier created successfully", supplier_schema.dump(supplier), 201)

@supplier_bp.route("", methods=["GET"])
@jwt_required()
def list_suppliers():
    suppliers = Supplier.query.all()
    return success_response("Suppliers retrieved", suppliers_schema.dump(suppliers))

@supplier_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_supplier(id):
    if not is_admin():
        return error_response("Admin role required", 403)

    supplier = Supplier.query.get(id)
    if not supplier:
        return error_response("Supplier not found", 404)

    db.session.delete(supplier)
    db.session.commit()
    return success_response("Supplier deleted successfully", None, 200)
