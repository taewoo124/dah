from django.shortcuts import render
from .models import Post


def list(request):
    posts = Post.objects.all().order_by('-created_at')
    # print(posts)

    return render(request, 'dashboard/post_list.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        post = Post.objects.create(title=title, body=body)

    print(post)

    return render(request, 'dashboard/post.html', {'post': post})


def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'dashboard/post_detail.html', {'post': post})
