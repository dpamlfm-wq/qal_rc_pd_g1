import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

headers = {
    "User-Agent": "QA Student"
}

response = requests.get(
    f"{BASE_URL}/posts",
    headers=headers
)

print("Статус код:", response.status_code)

assert response.status_code == 200

print("✅ Запит з headers виконано успішно!")