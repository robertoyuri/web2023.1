from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets import ClienteViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename="Cliente")

urlpatterns = [
    path('cep', views.cep, name='cep'),
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('login', views.login, name='login'),
    path('testejs', views.testjs, name='testejs'),
    path('read_cliente', views.read_cliente, name='read_cliente'),
    path('create_doctor', views.create_doctor, name='create_doctor'),
    path('create_cliente', views.create_cliente, name='create_cliente'),
    path("update_cliente/<int:id>", views.update_cliente, name='update_cliente'),
    path("delete_cliente/<int:id>", views.delete_cliente, name='delete_cliente'),
    path("api/", include(router.urls)),
]