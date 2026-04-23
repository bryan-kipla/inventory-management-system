from app.extensions import db
from app.models.product import Product
from app.models.category import Category
from app.schemas.product_schema import ProductSchema
from app.utils.responses import success_response, error_response

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def create_product(data, current_user):
    if current_user.role.name not in ["admin", "manager"]:
        return error_response("Only admin or manager can add products", 403)

    if not all([data.get("name"), data.get("category_id"), data.get("price")]):
        return error_response("Name, category_id, and price are required", 400)

    category = Category.query.get(data["category_id"])
    if not category:
        return error_response("Invalid category_id", 400)

    product = Product(name=data["name"], category=category, price=data["price"])
    db.session.add(product)
    db.session.commit()
    return success_response("Product created successfully", product_schema.dump(product), 201)

def list_products():
    products = Product.query.all()
    return success_response("Products retrieved", products_schema.dump(products))
