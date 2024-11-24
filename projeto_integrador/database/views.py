from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

# Exibe a lista de usuários
def user(request):
    users = User.objects.all()
    return render(request, 'pagina/index.html', {'users': users})

# Cria um novo usuário
@csrf_protect  # Aplicar proteção CSRF
def user_create(request):
    if request.method == 'POST':
        fullName = request.POST.get('nome')
        password = request.POST.get('senha')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        dateBirth = request.POST.get('data_nascimento')

        if not all([fullName,password,cpf,email,dateBirth]):
            return JsonResponse({"erro": "Todos os campos são obrigatorios"},status=400)
        
        user = User(
            fullName=fullName,
            password=password,
            cpf=cpf,
            email=email,
            dateBirth=dateBirth
        )
        user.save()

        message = "cadastro realizado com sucesso."
        
    return render(request, 'pagina/cadastro.html', {'message': message})



@csrf_protect
def login(request):
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')

        if not all([email, password]):
            return JsonResponse({"erro": "Todos os campos são obrigatorios"}, status=400)

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                message = "Login realizado com sucesso."
                # Redirecionar para a página desejada
                return redirect('pagina/index.html')
            else:
                message = "Senha incorreta."
        except User.DoesNotExist:
            message = "Usuário não encontrado."

    return render(request, 'pagina/index.html', {'message': message}) 
