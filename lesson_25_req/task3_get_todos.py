import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(
    f"{BASE_URL}/todos",
    params={"userId": 2}
)

print("Статус код:", response.status_code)

todos = response.json()

print("Кількість todo:", len(todos))

assert response.status_code == 200

for todo in todos:
    assert todo["userId"] == 2

print("✅ Усі записи належать користувачу 2")
