from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # POST 메서드는 db 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
    # 입력 폼 작성해서 전달(비어있는 form으로 다시생성) 
        form = ArticleForm()
    context = {
        'form' : form,
        'btn_name' : '글 생성'
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    # 수정할 글의 데이터를 불러온다
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
    # 수정 페이지를 나타내기 위해 form을 사용한다
    # 단, 수정할 데이터가 채워져 있는 형태여야 한다
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'btn_name' : '글 수정'
    }
    return render(request, 'articles/form.html', context)

def delete(request, pk):
    #  어떤 정보를 삭제할지 가져온다
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        # 데이터를 삭제한다.
        article.delete()
        return redirect('articles:index')
    
    # 삭제가 get으로 요청이 온다면
    return redirect('articles:detail', pk)