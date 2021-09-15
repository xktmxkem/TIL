from django.shortcuts import render


def index(request):
    title = 'title'
    return render(request, 'articles/index.html', {'name': 'ED'})


def greeting(request):
    foods = ['Apple', 'Banana', 'Peach']
    info = {
        'name': 'Ed',
    }
    
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    title = request.GET.get('title')

    context = {
        'title': title
    }
    return render(request, 'articles/catch.html', context)
    

def read(request, username):
    print(username)

    context = {
        'user': username,
    }
    return render(request, 'articles/read.html', context)