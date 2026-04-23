import pytest
from app import create_app
from app.extensions import db

@pytest.fixture
def test_app():
    app = create_app("instance.config.TestConfig")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(test_app):
    return test_app.test_client()
