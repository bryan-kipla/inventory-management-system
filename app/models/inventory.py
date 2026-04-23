from app.extensions import db
from app.models.product import Product

class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    product = db.relationship("Product", backref="inventory")
    quantity = db.Column(db.Integer, nullable=False)
