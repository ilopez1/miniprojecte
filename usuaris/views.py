# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
#from .forms import JugadorForm
from .forms import  RegistForm, LoginForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import *
from django.http import HttpResponseRedirect
from django.forms import modelform_factory
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages


def registrar(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            #email = cleaned_data.get('email')
            password = cleaned_data.get('password')
            usuari = User()
            usuari.username = username
            usuari.set_password(password)
            #usuari.email = email
            usuari.save()
            messages.success(request, 'Usuari Registrat!')
            return HttpResponseRedirect(reverse('usuaris:login'))
        else:
            messages.error(request, "Usuari ja existeix!")
    else:
        form=LoginForm()
    ctx={   'form':form,
            'capcelera':"Formulari de Registre"
        }
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'form.html', ctx )

def login(request):
    if request.method=='POST':
        form=LoginForm( request.POST )
        if form.is_valid():
            user=authenticate( username = form.cleaned_data['username'],
                               password = form.cleaned_data['password'])
            if user and user.is_active:
                authLogin( request, user )
                next = request.GET.get('next')
                return redirect(next or 'videos:llista_videos')

            else:
                messages.error(request,"Usuari o password incorrecte o usuari no actiu")
    else:
        form=LoginForm()
    ctx={   'form':form,
            'capcelera':"Formulari de Login"
        }
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'form.html', ctx )

def logout(request):
    authLogout( request )
    return redirect( 'usuaris:login' )
    
        
def index(request):
     return render(request,'index.html')