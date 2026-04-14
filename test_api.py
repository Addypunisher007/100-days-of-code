import requests

BASE_URL = "http://localhost:5001"

def test_valid_input():
    response = requests.post(f"{BASE_URL}/submit", json={"name": "Aditya"})
    assert response.status_code == 200

def test_missing_name():
    response = requests.post(f"{BASE_URL}/submit", json={})
    assert response.status_code == 400

def test_no_json():
    response = requests.post(f"{BASE_URL}/submit")
    assert response.status_code == 415