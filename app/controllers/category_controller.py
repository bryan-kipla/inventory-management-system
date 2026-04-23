from app.extensions import db
from app.models.category import Category
from app.schemas.category_schema import CategorySchema
from app.utils.responses import success_response, error_response

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

def create_category(data, current_user):
    if current_user.role.name != "admin":
        return error_response("Only admin can create categories", 403)

    if not data.get("name"):
        return error_response("Category name is required", 400)

    if Category.query.filter_by(name=data["name"]).first():
        return error_response("Category already exists", 409)

    category = Category(name=data["name"])
    db.session.add(category)
    db.session.commit()
    return success_response("Category created successfully", category_schema.dump(category), 201)

def list_categories():
    categories = Category.query.all()
    return success_response("Categories retrieved", categories_schema.dump(categories))
