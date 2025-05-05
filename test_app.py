# test_app.py
from app import app

def test_root_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World!'

def test_city_route():
    client = app.test_client()
    response = client.get('/city')
    assert response.status_code == 200
    assert response.data == b'minsk'

