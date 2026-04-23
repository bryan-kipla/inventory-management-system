from app import create_app
from app.extensions import db
from app.models.role import Role
from app.models.user import User

app = create_app()

with app.app_context():
    db.create_all()

    # Seed roles
    for role_name in ["admin", "manager", "user"]:
        if not Role.query.filter_by(name=role_name).first():
            db.session.add(Role(name=role_name))
    db.session.commit()

    # Seed admin user
    admin_role = Role.query.filter_by(name="admin").first()
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", email="admin@example.com", password="admin123", role=admin_role)
        db.session.add(admin)
        db.session.commit()
