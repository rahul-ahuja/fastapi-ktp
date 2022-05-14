from fastapi.testclient import TestClient
from main import app
from unittest import mock


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert b'Welcome to Stocks Trading!' in response.content
    
    
@mock.patch("main.requests.get")
def test_get_name(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(**{"status_code": 200, 
                                        "json.return_value": 
                                        {"companyName": "google", 
                                        "latestPrice": 123, 
                                        "symbol": "GOOGL"}})

    response = client.get("/stocks/GOOGL")
    assert response.status_code == 200
    assert b'The stock price of the google company currently is 123' in response.content
