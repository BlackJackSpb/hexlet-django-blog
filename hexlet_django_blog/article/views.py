from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Здесь в будущем можно будет добавить логику (например, получение статей из БД)
        articles = []  # заглушка, позже заменим
        return render(request, "articles/index.html", context={"articles": articles})
