from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)

    else:
        form = UserForm()
    
    return render(request, 'pagina/cadastro.html', {'form': form})  # Caminho ajustado

def success(request):
    return render(request, 'pagina/success.html')  # Caminho ajustado
