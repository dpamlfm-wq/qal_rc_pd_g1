from django.shortcuts import render
from django.http import Http404


USERS = {
    "olena": {
        "email": "olena@example.com",
        "role": "student"
    },
    "john": {
        "email": "john@example.com",
        "role": "admin"
    }
}


POSTS = {
    1: {
        "title": "Перший пост",
        "content": "Я вивчаю Django."
    },
    2: {
        "title": "Другий пост",
        "content": "Маршрутизація працює."
    }
}


def home(request):
    return render(
        request,
        "home.html",
        {
            "title": "Головна сторінка",
            "text": "Це моя перша сторінка на Django."
        }
    )


def about(request):
    return render(
        request,
        "about.html",
        {
            "title": "Про мене",
            "text": "Мене звати Olena. Я вивчаю Django та Python."
        }
    )


def user_profile(request, username):

    user = USERS.get(username)

    if user is None:
        raise Http404("Користувача не знайдено")

    return render(
        request,
        "profile.html",
        {
            "username": username,
            "email": user["email"],
            "role": user["role"]
        }
    )


def post_detail(request, post_id):

    post = POSTS.get(post_id)

    if post is None:
        raise Http404("Пост не знайдено")

    return render(
        request,
        "post.html",
        {
            "post_id": post_id,
            "title": post["title"],
            "content": post["content"]
        }
    )


def products(request):

    return render(
        request,
        "products.html",
        {
            "title": "Мої товари",
            "products": [
                "Laptop",
                "Mouse",
                "Keyboard",
                "Monitor"
            ]
        }
    )