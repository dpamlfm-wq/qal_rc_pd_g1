import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


response = requests.get(f"{BASE_URL}/posts")

print("Статус код:", response.status_code)

posts = response.json()

print("Кількість записів:", len(posts))

assert response.status_code == 200
assert len(posts) == 100

print("✅ Успішно перевірено!")
