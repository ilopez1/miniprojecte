from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username=forms.CharField(label="User",
                             max_length=16,
                             )
    password=forms.CharField(label="Password",
                             max_length=24,
                             widget=forms.PasswordInput(),
                             )
                             
class RegistForm (forms.Form):
    username = forms.CharField(max_length = 100)
    #email = forms.EmailField()
    password = forms.CharField(min_length=4, widget=forms.PasswordInput())

    def clean_username(self):
        ##-------Comproba que no existeix aquest user-------##
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nom usuari ja existent.')
        return username