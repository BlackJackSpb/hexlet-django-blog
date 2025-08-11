# hexlet_django_blog/article/urls.py
from django.urls import path
from .views import (
IndexView,
ArticleView,
ArticleFormCreateView,
ArticleFormEditView,
ArticleFormDeleteView
)


app_name = "article"


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='show'),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="update"),
    path('create/', ArticleFormCreateView.as_view(), name='create'),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="delete"),
]
