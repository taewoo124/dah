from django.shortcuts import render, get_object_or_404

from .models import Post

from dashboard.forms import PostForm


def list(request, pk=None):
    context = {}
    posts = Post.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            body = form.cleaned_data.get('body')

            Post.objects.create(title=title, description=description, body=body)

    elif request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()

        return render(request, 'dashboard/post_list.html', {'posts': posts})

    else:
        form = PostForm()

    context['form'] = form
    context['posts'] = posts

    return render(request, 'dashboard/post_list.html', context)


def detail(request, pk=None):
    post = Post.objects.get(id=pk)

    return render(request, 'dashboard/post_detail.html', {'post': post})
