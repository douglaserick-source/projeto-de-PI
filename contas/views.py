from django.shortcuts import render

def login_view(request):
    return render(request, 'contas/login.html')

def cadastro_view(request):
    return render(request, 'contas/cadastro.html')

def perfil_view(request):
    return render(request, 'contas/perfil.html')