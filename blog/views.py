from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
from django.core.urlresolvers import reverse


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            url = reverse('blog:detail', args=[post.pk])
            return redirect(url)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})