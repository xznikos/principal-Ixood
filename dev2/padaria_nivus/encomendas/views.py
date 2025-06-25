from django.shortcuts import render, redirect, get_object_or_404
from .forms import EncomendasForm
from .models import EncomendasModel
from django.http import HttpRequest

def encomendas_home(request):
    contexto = {
        "encomendas": EncomendasModel.objects.all()
    }
    return render(request,'encomendas/home.html', contexto)

def adicionar_home(request):
    if request.method == "POST":
        formulario = EncomendasForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("encomendas:home")
        
    else:
        formulario = EncomendasForm()
    contexto = {
        "form": formulario
    }
    return render(request,'encomendas/adicionar.html', contexto)

def remover_home(request:HttpRequest, id):
    encomenda = get_object_or_404(EncomendasModel, id=id)
    encomenda.delete()
    return redirect("encomendas:home")

def editar_encomenda(request, id):
    encomenda = get_object_or_404(EncomendasModel, id=id)
    if request.method == "POST":
        formulario = EncomendasForm(request.POST, request.FILES, instance=encomenda)
        if formulario.is_valid():
            formulario.save()
            return redirect("encomendas:home")
    else:
        formulario = EncomendasForm(instance=encomenda)

    contexto = {
        "form": formulario
    }
    return render(request, 'encomendas/editar.html', contexto)

def teste_home(request):
    return render(request, 'teste.html')

# Create your views here.
