from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    # todos = Todo.object.all() # 모든 데이터를 받아옴
    # 내가 작성한 데이터만 보자!
    # 유저 정보를 바탕으로 todo의 역참조로 작성한 글만 조회한 데이터를 todos에 저장 
    author = request.user
    todos = author.todo_set.all() # 역참조로 내가 작성한 글만 조회
    context = {
        'todos' : todos
    }
    return render(request, 'todos/idex.html', context)

def new(request):
    if request.method == "POST":
        form = TodoForm()
        if form.is_valid():
            # commit을 하지 않고 세이브 되기 직전의 상태의 정보를 todo에 가져옴
            todo = form.save(commit=False)
            # 가져온 todo에서 author 권한자 를 유저로 바꿔주면 해당 만든 자료는 author에 저장된 user만 접근 가능하도록 만들 수 있음
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form' : form, 
    }
    return render(request, 'todos/new.html', context)