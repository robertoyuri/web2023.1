from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('login', views.login, name='login'),
    path('testejs', views.testjs, name='testejs'),
    path('create_doctor', views.create_doctor, name='create_doctor'),
    path('create_cliente', views.create_cliente, name='create_cliente'),
    path('read_cliente', views.read_cliente, name='read_cliente'),
    path("update_cliente/<int:id>", views.update_cliente, name='update_cliente'),
    path("delete_cliente/<int:id>", views.delete_cliente, name='delete_cliente'),
]