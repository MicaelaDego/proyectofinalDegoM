from ast import Index
from django.urls import path, URLPattern
from Appperfil.views import  * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('actualizarusuario/', actualizar_usuario , name= 'actualizar'),



   
  
]