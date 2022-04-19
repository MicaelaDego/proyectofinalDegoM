
from django.db import models
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your models here.
class Post (models.Model):
    titulo = models.CharField(max_length=40, primary_key=True)
    subtitulo = models.CharField(max_length=100)
    introduccion = models.CharField(max_length=400)
    cuerpo = models.CharField(max_length=2000)
    autor = models.CharField(max_length=40)
    fecha  = models.DateField()
    imagen= models.ImageField()