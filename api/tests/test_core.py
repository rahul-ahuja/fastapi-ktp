from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    
def test_get_name():
    response = client.get("/stocks/GOOGL")
    assert response.status_code == 200
