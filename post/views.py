from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DetailView
# Create your views here.





class PostList(ListView):
    model = Post           ##in template [object_list , post_list]
    # context_object_name = 'all_posts'
    ordering = ['created_at']
    # queryset = Post.objects.filter(active=True)
    # template_name = 'post/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname']= 'ahmed'
        return context




    def get_queryset(self):
        return Post.objects.filter(active=True)
    



class PostDetail(DetailView):
    model = Post




class PostCreate():
    pass




class PostUpdate():
    pass



class PostDelete():
    pass