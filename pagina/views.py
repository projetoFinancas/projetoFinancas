from django.shortcuts import render


def index(request):
    return render(request, 'pagina/index.html')

def dashboard(request):
    return render(request, 'pagina/dashboard.html')


def cadastro(request):
    return render(request, 'pagina/cadastro.html')
