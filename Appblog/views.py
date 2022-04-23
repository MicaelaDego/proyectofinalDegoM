from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from Appblog.models import *
from django.template import loader
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from Appperfil.models import Avatar

# Create your views here.
def perfil (request):
    avatar = Avatar.objects.filter(user= request.user)

    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
        return render (request, 'Appblog/perfil.html', {'url': avatar[0].imagen.url })
    return render (request, 'Appblog/perfil.html')

class Listpost (ListView):
    model = Post
    template_name = "Appblog/post_list.html"



class Detailpost (DetailView):
    model = Post
    template_name = "Appblog/post_detail.html"

class Createpost (LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/Appblog/postlist"
    fields = ['titulo', 'subtitulo', 'introduccion' , 'cuerpo', 'autor', 'fecha']

class Updatepost (LoginRequiredMixin, UpdateView):
    model = Post
    success_url = "/Appblog/postlist"
    fields = ['titulo', 'subtitulo', 'introduccion' , 'cuerpo', 'autor', 'fecha']

class Deletepost (LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/Appblog/postlist"



def login_request (request):
    if request.method == 'POST':
        formulario = AuthenticationForm (request, data = request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            username = data ['username']
            password = data ['password']

            usuario = authenticate (username = username , password = password)

            if usuario is not None:
                login (request, usuario)
                return redirect ( 'List' )
            else: 
               return render (request, 'Appblog/inicio.html', {'errors': ['El usuario no existe']})
        else:
            return render (request, 'Appblog/inicio.html', {'errors': ['Revise los datos indicados']})
    else:
        form = AuthenticationForm()
        return render (request, 'Appblog/login.html', {'form': form})

def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get ('username')
            return redirect ( 'List' )
        else:
            return render (request, 'Appblog/inicio.html', {'errors': ['No se cumplieron las validaciones']})
    else:
        form = UserCreationForm()
        return render (request, 'Appblog/register.html', {'form': form })


