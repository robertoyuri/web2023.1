from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('login', views.login, name='login'),
    path('create_doctor', views.create_doctor, name='create_doctor'),
]