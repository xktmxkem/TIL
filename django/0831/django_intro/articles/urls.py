from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('read/<username>/<article_number>/',views.read, name='read'),
    path('catch/',views.catch, name = 'catch'),
    path('throw/', views.throw, name = 'throw'),
    path('greeting/', views.greeting, name= 'greeting'),
    path('articles/index/', views.index, name = 'index'),
]
