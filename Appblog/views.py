from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from Appblog.models import *
from django.template import loader
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def inicio (request,):
    return render (request, 'Appblog/inicio.html')

class Listpost (ListView):
    model = Post
    template_name = "Appblog/post_list.html"

class Detailpost (DetailView):
    model = Post
    template_name = "Appblog/post_detail.html"

class Createpost (CreateView):
    model = Post
    success_url = "/Appblog/post/list"
    fields = ['titulo', 'subtitulo', 'introduccion' , 'cuerpo', 'autor', 'fecha']

class Updatepost (UpdateView):
    model = Post
    success_url = "/Appblog/post/list"
    fields = ['titulo', 'subtitulo', 'introduccion' , 'cuerpo', 'autor', 'fecha']

class Deletepost (DeleteView):
    model = Post
    success_url = "/Appblog/post/list"
