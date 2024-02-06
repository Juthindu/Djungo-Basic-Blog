from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
  Posts = Post.objects.all()
  return render(request,'index.html',{'Posts': Posts})


def post(request, pk):
  Posts = Post.objects.get(id=pk)
  return render(request,'post.html',{'Posts': Posts})