from urllib import request
from django.http import HttpResponse
from django.template import loader
from dataclasses import fields

from django.shortcuts import render
from Appperfil.forms import *
from Appperfil.models import *


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect



# Create your views here.
@login_required()
def actualizar_usuario (request):
    usuario = request.user 

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data ['email']
            usuario.passwor1 = data ['password1']
            usuario.password2 = data ['password2']
            usuario.first_name = data ['first_name']
            usuario.last_name = data ['last_name']

            usuario.save()

            return redirect ('List')
        else:
            formulario = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username })
            return render (request, 'Appperfil/editar_usuario.html', {'form': formulario, 'errors': ['Datos invalidos'] })

    else:
        formulario = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username })
        return render (request, 'Appperfil/editar_usuario.html', {'form': formulario })

@login_required


@login_required()
def cargar_imagen(request):

    if request.method == "POST":

        formulario = Avatarformulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("List")
    else:

        formulario = Avatarformulario()
        return render(request, "Appperfil/cargar_imagen.html", {"form": formulario}) 
 




