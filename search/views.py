from django.shortcuts import render
from blog.models import Post

# Create your views here.
def do_search(request):
    posts = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, "blog/home.html", {"posts": posts})
