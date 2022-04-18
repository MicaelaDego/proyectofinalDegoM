from ast import Index
from django.urls import path, URLPattern
from Appblog.views import  * 


urlpatterns = [
    path('Inicio/', inicio, name= 'inicio'),
    path('post/list' , Listpost.as_view(), name = 'List'),
    path('nuevo/', Createpost.as_view(), name='New'), 
    path('<pk>/', Detailpost.as_view(), name = 'Detail'), 
    path('editar/<pk>', Updatepost.as_view(), name= 'Edit'),
    path('borrar/<pk>', Deletepost.as_view(), name = 'Delete'),
    

   
  
]