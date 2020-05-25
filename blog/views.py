from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def blog(request):
    allpost = Post.objects.all()
    print(allpost)
    context = {'allpost':allpost}
    return render(request,'blog/blog.html',context)

def post(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request,'blog/post.html',context)

