from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["who"] = "World"
        return contex


def about(request):
    return  render(request, "about.html")