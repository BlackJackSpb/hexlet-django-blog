# hexlet_django_blog/article/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import ArticleForm
from django.contrib import messages
from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])  # ← автоматически 404, если нет
        return render(
            request,
            'articles/show.html',
            context={'article': article}
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно создана!')  # ← флеш-сообщение
            return redirect('article:index')
        # Если форма невалидна — показываем её снова с ошибками
        return render(request, 'articles/create.html', {'form': form})