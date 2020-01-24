import urllib.parse
from django.shortcuts import render
from .models import Category, Post, Comment

# Create your views here.
from blogo.models import Post
from .forms import CommentForm
from django.contrib.auth.models import User


def blogo_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, "blogo_index.html", context)


def blogo_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blogo_category.html", context)


def blogo_detail(request, pk):
    post = Post.objects.get(pk=pk)
    share_string = urllib.parse.quote(post.content)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "share_string": share_string,
    }

    return render(request, "blogo_detail.html", context)


def blogo_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blogo_detail.html", context)