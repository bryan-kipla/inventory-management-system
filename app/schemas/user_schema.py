from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.user import User
from app.extensions import db

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
