from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)    

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'articles':article}
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(
        title=title,
        content=content
    )
    article.save()

    # forward 방식 :요청, 응답 정보를 그대로 계속 가져감, 페이지만 바뀐다.
    # 시스템에 변화가 생기지 않는 단순 조회 요청
    # redirect 방식 : 새로운 요청을 생성(기존 요청, 응답 정보가 제거됨) => url 변경
    # 시스템에 변화가 생기는 새로운 요청
    # return redirect('articles:detail", article.pk)
    return redirect("articles:detail", article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)