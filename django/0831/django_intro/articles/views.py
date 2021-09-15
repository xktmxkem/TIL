from django.shortcuts import render
import random
# Create your views here.
# 필수 사항 인자를 하나 받아야 한다. 
# 미들웨어에서 인자를 넘겨주기 때문에 반드시 있어야한다. 
# render : html을 이쁘게 보이게 하는 모듈
# html파일은 반드시 templates 폴더를 만들어 내부에 이름으로 html로 작성한다.
def index(request):
    # 만약 db관련 업무가 있다면
    # 파이썬 코드로 처리 
    title = 'title'
    return render(request, 'articles/index.html', {'name' : ' ED'})

def greeting(request):
    foods = ['Apple', 'Banana', 'Peach']
    info = {
        'name' : 'hoon'
    }
    context = {
        'food' : foods,
        'info' : info,
    }

    return render(request, 'articles/greeting.html', context)



def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    title = request.GET.get('title')

    context = {
        "title" : title
    }
    return render(request, 'articles/catch.html', context)
    
def read(request, username, article_number):
    print(username)
    print(article_number)

    context = {
        'user' : username,
        'article' : article_number,
    }
    
    return render(request, 'articles/read.html', context)