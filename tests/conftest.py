import pytest
from src import create_app
from src import db

@pytest.fixture()
def app():
    app = create_app("sqlite://")
    
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        
    yield app
    
    
@pytest.fixture()
def client(app):
    return app.test_client()
    
    