# hexlet_django_blog/article/forms.py
from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]