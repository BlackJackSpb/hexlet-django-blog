# hexlet_django_blog/article/urls.py
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]