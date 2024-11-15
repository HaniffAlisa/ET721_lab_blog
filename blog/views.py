from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'post_list.html')
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    # Form logic for creating a post
    pass

def post_edit(request, pk):
    # Form logic for editing a post
    pass
    