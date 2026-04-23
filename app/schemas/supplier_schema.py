from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.supplier import Supplier
from app.extensions import db

class SupplierSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        load_instance = True
        sqla_session = db.session
