from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def create_doctor(request):
    return render(request, 'create_doctor.html')

def login(request):
    return render(request, 'login.html')