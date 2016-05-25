from django.shortcuts import render
from .models import Post, Comment

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})