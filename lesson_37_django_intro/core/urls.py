from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "users/<str:username>/",
        views.user_profile,
        name="user_profile"
    ),

    path(
        "posts/<int:post_id>/",
        views.post_detail,
        name="post_detail"
    ),

    path(
        "products/",
        views.products,
        name="products"
    ),
]
