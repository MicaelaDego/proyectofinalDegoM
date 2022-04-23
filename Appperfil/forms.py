
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir contraseña', widget= forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}

class UserEditForm (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir contraseña', widget= forms.PasswordInput)
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label= 'Apellido')

    class Meta:
        model = User 
        fields = ['first_name', 'last_name' ,'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}

class Avatarformulario (forms.Form):
    imagen = forms.ImageField()

