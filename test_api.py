from app import app

client = app.test_client()

response = client.get('/data')

print("Status Code:", response.status_code)

data = response.get_json()

if response.status_code == 200:
    print("✅ Status Test Passed")

if data["name"] == "Aditya":
    print("✅ Data Test Passed")

print("✅ CI Test Completed")