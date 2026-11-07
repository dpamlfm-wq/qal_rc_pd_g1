from django.shortcuts import render


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