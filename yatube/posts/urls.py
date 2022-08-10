from django.urls import include, path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group_list/', views.group_posts, name='group_posts')
    # Отдельная страница с информацией о сорте мороженого
    #path('group/<slug:slug>/', views.group_posts()),
]