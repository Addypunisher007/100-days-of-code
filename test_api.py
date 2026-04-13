import requests

url = "http://localhost:5000/data"

response = requests.get(url)

print("Status Code:", response.status_code)

# Test 1: Status Code
if response.status_code == 200:
    print("✅ Status Code Test Passed")
else:
    print("❌ Status Code Test Failed")

# Test 2: Response Content
data = response.json()

if data.get("name") == "Aditya":
    print("✅ Name Test Passed")
else:
    print("❌ Name Test Failed")

if data.get("role") == "DevOps Learner":
    print("✅ Role Test Passed")
else:
    print("❌ Role Test Failed")

# Test 3: Negative Test (wrong endpoint)
bad_response = requests.get("http://localhost:5000/wrong")

if bad_response.status_code == 404:
    print("✅ Negative Test Passed (404)")
else:
    print("❌ Negative Test Failed")