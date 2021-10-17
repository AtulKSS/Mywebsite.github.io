from django import http
from django.contrib import admin
from django.contrib.auth import forms
from django.urls import path
from home import views
urlpatterns = [
   path("",views.index, name='home'),
   path("contact",views.contact, name ='contact'),
   path("about",views.about, name ='about'),
   path("link",views.link, name ='link'),
   path("login",views.loginuser, name ='login'),
   path("logoutuser",views.logoutuser, name ='logoutuser'),
   path("loggedinn",views.logged, name ='loggedinn'),
   path("signup",views.signup, name ='signup'),
]
