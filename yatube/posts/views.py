from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница со списком групп
"""def group_posts(request, slug):
    return HttpResponse(f'Список групп {slug}')
"""
