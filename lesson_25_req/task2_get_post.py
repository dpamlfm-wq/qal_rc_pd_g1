import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/10")

print("Статус код:", response.status_code)

post = response.json()

print("ID:", post["id"])
print("User ID:", post["userId"])
print("Title:", post["title"])

assert response.status_code == 200
assert post["id"] == 10

assert "userId" in post
assert "id" in post
assert "title" in post
assert "body" in post

print("✅ Post успішно перевірено!")