from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 0, widget = forms.TextInput(
        attrs = {'class': 'form-control-inputs', 'placeholder': 'Username'}) )

    password1 = forms.CharField(label = 0, widget = forms.PasswordInput(
        attrs = {'class': 'form-control-inputs', 'placeholder': 'Password (at least 8 characters)'}) )

    password2 = forms.CharField(label = 0, widget = forms.PasswordInput(
        attrs = {'class': 'form-control-inputs', 'placeholder': 'Password repeat'}) )

    email = forms.EmailField(label = 0, widget = forms.EmailInput(
        attrs = {'class': 'form-control-inputs', 'name': 'email', 'placeholder': 'Email'}))
    
    



    class Meta():
        model = User
        fields = ('username','email', 'password1', 'password2')

        def __str__(self):
            return User.username

