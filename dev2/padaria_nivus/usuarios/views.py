from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        # Verifica se o usuário já existe
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            User.objects.create_user(username=usuario, password=senha)
            messages.success(request, 'Usuário criado com sucesso! Faça login.')
            return redirect('usuarios:login')
    return render(request, 'usuarios/cadastro.html')

def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('encomendas:home')  # Ajuste para sua página principal
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'usuarios/login.html')

def deslogar(request):
    logout(request)
    return redirect('usuarios:login')