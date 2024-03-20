from django.shortcuts import render
from .models import Post


def list(request):
    print(f'{request.POST = }', 'LIST')

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        Post.objects.create(title=title, body=body)

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'dashboard/post_list.html', {'posts': posts})


def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'dashboard/post_detail.html', {'post': post})
