import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.post(
    f"{BASE_URL}/posts",
    json={}
)

print("Статус код:", response.status_code)
print(response.json())

print("✅ Перевірку виконано")