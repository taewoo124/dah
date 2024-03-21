from django.shortcuts import render
from .models import Post

from dashboard.forms import PostForm


def list(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            Post.objects.create(title=title, body=body)
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'dashboard/post_list.html', {'posts': posts, 'form': form})


def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'dashboard/post_detail.html', {'post': post})
