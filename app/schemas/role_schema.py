from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.role import Role
from app.extensions import db

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        sqla_session = db.session
