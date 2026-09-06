from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get('/healthz').status_code == 200

def test_ready():
    assert client.get('/readyz').json()['status'] == 'ready'

def test_metrics():
    assert client.get('/metrics').status_code == 200

def test_api():
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'
