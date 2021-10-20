from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo

def index(request):
    # todos = Todo.objects.all() # 모든 데이터를 받아옴
    # 내가 작성한 데이터만 보자!
    author = request.user
    todos = author.todo_set.all() # 역참조로 내가 작성한 글만 조회
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)