from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    article_list = Article.objects.all()
    return render(request, 'board/index.html', {'article_list': article_list})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    article.hit()
    return render(request, 'board/detail.html', {'article': article})