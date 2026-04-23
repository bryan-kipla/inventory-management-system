from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.product import Product
from app.extensions import db

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session
