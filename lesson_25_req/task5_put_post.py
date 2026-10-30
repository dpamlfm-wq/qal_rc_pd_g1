import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

payload = {
    "id": 5,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}

response = requests.put(
    f"{BASE_URL}/posts/5",
    json=payload
)

print("Статус код:", response.status_code)

post = response.json()

print(post)

assert response.status_code == 200
assert post["title"] == "updated title"
assert post["body"] == "updated body"

print("✅ PUT успішно виконано!")