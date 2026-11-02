import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

payload = {
    "title": "my title",
    "body": "my body",
    "userId": 1
}

response = requests.post(
    f"{BASE_URL}/posts",
    json=payload
)

print("Статус код:", response.status_code)

post = response.json()

print(post)

assert response.status_code == 201
assert post["title"] == payload["title"]
assert post["body"] == payload["body"]
assert post["userId"] == payload["userId"]

print("✅ Post успішно створено!")