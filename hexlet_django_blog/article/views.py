from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        # Обрабатываем GET-запрос с параметрами tags (str) и article_id (int)
        context = {
            'tags': tags,
            'article_id': article_id
        }
        return render(request, 'articles/index.html', context)
