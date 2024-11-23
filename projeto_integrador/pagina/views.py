from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'pagina/index.html')

def dashboard(request):
    return render(request, 'pagina/dashboard.html')


def cadastro(request):
    return render(request, 'pagina/cadastro.html')

@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')  # Obtém a mensagem do usuário
        print(f"Recebido do usuário: {user_input}")  # Verifique se a mensagem está chegando

        # Lógica do chatbot
        if user_input == "1":
            response = "Você escolheu a opção 'Consultar CPF'. Aqui ficará o código para verificar o CPF."
        elif user_input == "2":
            response = """Você escolheu o Assistente Financeiro! Aqui estão as opções de dicas:
            1 - Dicas de Planejamento Financeiro
            2 - Dicas para Reduzir Dívidas
            3 - Dicas para Poupar e Investir
            4 - Dicas de Consumo Consciente
            5 - Dicas de Crédito"""
        elif user_input == "1-1":
            response = "Dicas de Planejamento Financeiro: Faça um orçamento mensal detalhado e siga-o rigorosamente."
        elif user_input == "1-2":
            response = "Dicas para Reduzir Dívidas: Pague dívidas de maior juros primeiro e renegocie suas condições."
        elif user_input == "1-3":
            response = "Dicas para Poupar e Investir: Reserve 10% da sua renda mensal para uma poupança ou investimentos."
        elif user_input == "1-4":
            response = "Dicas de Consumo Consciente: Evite compras impulsivas, avalie a necessidade antes de comprar."
        elif user_input == "1-5":
            response = "Dicas de Crédito: Use crédito com responsabilidade, sempre priorizando os juros mais baixos."
        else:
            response = """Escolha uma das opções abaixo para começar:
            1 - Consultar CPF
            2 - Assistente Financeiro"""

        print(f"Resposta do bot: {response}")  # Verifique a resposta do bot
        # Retorna a resposta como JSON
        return JsonResponse({"response": response})

    return JsonResponse({"error": "Método não permitido."}, status=405)
