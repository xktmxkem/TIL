"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views as art_views
from accounts import views as acc_views

# view에서 할것(함수)을 넘겨주면 된다. 
# path 뒤에 함수를 인자로 넘겨서 (python은 1급객체라 가능함) 작동시킴
# admin/이 들ㅇ오면 admin.site.urls 라는 함수가 실행되게 된다. 
# 제일 위부터 항상 검사함
# variable routing를 사용할때는 다른 routing과는 다르게 앞에 다른 이름을 넣는것이 좋다
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    # path('accounts/index/', acc_views.index,),
    path('articles/', include('articles.urls')),
    # articles app
    # path('read/<username>/<article_number>/',art_views.read),
    # path('catch/',art_views.catch),
    # path('throw/',art_views.throw),
    # path('greeting/',art_views.greeting),
    # path('articles/index/',art_views.index),
    path('admin/', admin.site.urls),
]
