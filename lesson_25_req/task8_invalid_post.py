import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(
    f"{BASE_URL}/posts/999999"
)

print("Статус код:", response.status_code)
print("Відповідь:", response.text)

assert response.status_code == 404 or response.json() == {}

print("✅ Негативний тест пройдено!")