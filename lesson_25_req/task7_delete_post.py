import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.delete(
    f"{BASE_URL}/posts/5"
)

print("Статус код:", response.status_code)

assert response.status_code in [200, 204]

print("✅ DELETE успішно виконано!")