# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username=forms.CharField(label="Nom usuari",
                             max_length=16,
                             help_text="Nom d'usuari.")
    password=forms.CharField(label="Paraula de pas",
                             max_length=24,
                             help_text="Paraula de pas per accedir a sistema.",
                             widget=forms.PasswordInput(),
                             )

    

class RegistForm (forms.Form):
    username = forms.CharField(max_length = 100)
    email = forms.EmailField()
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())

    def clean_username(self):
        ##-------Comproba que no existeix aquest user-------##
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nom usuari ja existent.')
        return username