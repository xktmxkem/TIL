from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):

    return render(request, 'articles/new.html' )

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()


    # 코드가 중복되기에 index를 여기에서 요청!!
    # redirect(요청경로) 
    return redirect('articles:index')




    # 코드가 중복되기에 index를 여기서 요청 
    #     articles = Article.objects.all()
    # context = {
    #     'article' : articles
    # }

    # return render(request, 'articles/index.html', context)

def detail(request, pk):
    # 글하나를 조회한다
    article = Article.objects.get(pk = pk)
    # 조회된 data를 html에 보여준다 
    context = {
        'article' : article,
    }

    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    # 어떤 글 수정??
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }

    return render(request, 'articles/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터를 수정해서 저장하자!!
    article = Article.objects.get(pk=pk) # 수정할 원본 데이터를 불러오자!
    article.title = title
    article.content = content
    article.save()
    # 저장이 끝나면 디테일 페이지로 돌아가자
    # context = {
    #     'article' : article,
    # }
    # return render(request, 'article/detail.html', context)

    return redirect('articles:detail' , article.pk)

def delete(request, pk):
    # POST 요청일 때 
    if request.method == 'POST':
        # 데이터를 삭제한다!
        article = Article.objects.get(pk=pk)
        article.delete()
        # 글 목록페이지로 이동한다.
        return redirect('articles:index')

    else:
        return redirect('articles:detail', pk)