from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.category import Category
from app.extensions import db

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db.session
