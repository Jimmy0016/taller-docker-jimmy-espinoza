import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_suma_route(client):
    response = client.get('/suma/2/3')
    data = response.get_json()
    assert data["resultado"] == 5

# Test temporal fallido eliminado  comentado
# def test_fallo_temporal():
#     assert 1 == 2
