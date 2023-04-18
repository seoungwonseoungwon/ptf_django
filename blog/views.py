from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'

# def index(request):
#     posts = Post.objects.all().order_by('-pk')


#     return render(request, 'blog/index.html',{'posts':posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/post_detail.html', {'post':post})