from django.shortcuts import render, redirect
from user.models import User, Profile
from post.models import Post


def get_posts(request):
    posts = Post.objects.all()
    return render(request, "list.html", {'posts': posts})


def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "detail.html", {'post': post})


def create_post(request):
    if request.method == "POST":
        user = User.objects.get(username='asan')
        post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=user,
        )
        return redirect('post:post-detail', pk=post.pk)
    return render(request, "create.html")


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.title = request.POST.get('title', post.title)
        post.content = request.POST.get('content', post.content)
        post.save()
        return redirect('post:post-detail', pk=post.pk)
    return render(request, "edit.html", {'post': post})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post:post-list')
