from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'post'
