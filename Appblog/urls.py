from ast import Index
from django.urls import path, URLPattern
from Appblog.views import  * 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('Inicio/', inicio, name= 'inicio'),

    path('login/', login_request, name= 'Login'),
    path('register/', register, name = 'Register'),
    path('logout/', LogoutView.as_view (template_name= 'Appblog/logout.html'), name ='Logout' ),
    path('postlist' , Listpost.as_view(), name = 'List'),
    path('nuevo/', Createpost.as_view(), name='New'), 
    path('<pk>/', Detailpost.as_view(), name = 'Detail'), 
    path('editar/<pk>', Updatepost.as_view(), name= 'Edit'),
    path('borrar/<pk>', Deletepost.as_view(), name = 'Delete'),


   
  
]