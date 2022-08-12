from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Post, Group

# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': "Это главная страница проекта Yatube",
        'posts': posts
    }
    return render(request, template, context)


# Страница со списком групп
def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Список групп {slug}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
        'group': group,
    }
    return render(request, template, context)
