import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    response = client.get('/')
    assert b'Hello Sharan' in response.data

def test_home_devops_message(client):
    response = client.get('/')
    assert b'DevOps' in response.data

def test_invalid_route(client):
    response = client.get('/invalid')
    assert response.status_code == 404
