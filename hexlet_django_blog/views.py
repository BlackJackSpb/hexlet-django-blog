# hexlet_django_blog/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


def about(request):
    return render(request, "about.html")
