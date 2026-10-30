import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

payload = {
    "title": "patched title"
}

response = requests.patch(
    f"{BASE_URL}/posts/1",
    json=payload
)

print("Статус код:", response.status_code)

post = response.json()

print(post)

assert response.status_code == 200
assert post["title"] == "patched title"

print("✅ PATCH успішно виконано!")