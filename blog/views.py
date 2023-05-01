from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView
# Create your views here.





class PostList(ListView):
    model = Post
    paginate_by = 1




class PostDetail(DetailView):
    model = Post    