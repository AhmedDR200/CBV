from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DetailView
# Create your views here.





class PostList(ListView):
    model = Post




class PostDetail(DetailView):
    model = Post




class PostCreate():
    pass




class PostUpdate():
    pass



class PostDelete():
    pass