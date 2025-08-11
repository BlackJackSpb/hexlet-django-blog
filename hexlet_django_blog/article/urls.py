# hexlet_django_blog/article/urls.py
from django.urls import path
from .views import IndexView, ArticleView, ArticleFormCreateView


app_name = "article"


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='show'),
    path('create/', ArticleFormCreateView.as_view(), name='create'),
]
