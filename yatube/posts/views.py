from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
        'text': "Это главная страница проекта Yatube"
    }
    return render(request, template, context)


# Страница со списком групп
def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Список групп'
    context = {
        'title': title,
        'text': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)
