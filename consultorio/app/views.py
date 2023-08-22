from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
# Create your views here.

def test(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def create_doctor(request):
    return render(request, 'create_doctor.html')

def create_cliente(request):
    cliente_form = ClienteForm(request.POST or None, request.FILES or None)
    if(cliente_form.is_valid()):
        cliente = cliente_form.save(commit=False)
        cliente.save()
        return redirect("read_cliente")
    return render(request, 'create_cliente.html', {'cliente_form':cliente_form})

def read_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_read.html', {'clientes':clientes})

def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente_form = ClienteForm(request.POST or None,
                               request.FILES or None,
                               instance=cliente)
    if(cliente_form.is_valid()):
        cliente = cliente_form.save(commit=False)
        cliente.save()
        return redirect("read_cliente")
    return render(request, 'create_cliente.html', {'cliente_form':cliente_form})

def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect("read_cliente")

def login(request):
    return render(request, 'login.html')

def testjs(request):
    return render(request, 'testjs.html')

def cep(request):
    return render(request, 'cep.html')