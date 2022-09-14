from django.shortcuts import render
from .models import Post
# Create your views here.
def posts(request):
  posts = Post.objects.all().order_by('date')
  return render(request,'posts/posts.html',{'posts':posts})

def post(request,slug):
  post = Post.objects.filter(slug = slug)
  return render(request,'posts/post.html',{'post':post})