"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Appblog.views import *
from Appmensaje.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Appblog/', include ('Appblog.urls')),
    path('Appperfil/', include ('Appperfil.urls')),
    path('Appmensajes/', include('Appmensaje.urls')),


    # url App BLOG 

    path('login/', login_request, name= 'Login'),
    path('register/', register, name = 'Register'),
     path('' , Listpost.as_view(), name = 'List'),
    path('logout/', LogoutView.as_view (template_name= 'Appblog/logout.html'), name ='Logout' ),
    path('nuevo/', Createpost.as_view(), name='New'), 
    path('<pk>/', Detailpost.as_view(), name = 'Detail'), 
    path('editar/<pk>', Updatepost.as_view(), name= 'Edit'),
    path('borrar/<pk>', Deletepost.as_view(), name = 'Delete'),
    path('about', about, name = 'about'),

    # url App MENSAJES
    




   

]

#URL de Login

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

LOGIN_URL = "/Appblog/login/"
