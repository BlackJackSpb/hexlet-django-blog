# hexlet_django_blog/article/urls.py
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('<str:tags>/<int:article_id>/', views.IndexView.as_view(), name='article'),
]
