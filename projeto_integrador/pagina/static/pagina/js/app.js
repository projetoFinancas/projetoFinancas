// Função para abrir/fechar o chat
function toggleChat() {
    const chat = document.querySelector('.chat');
    const chatBox = document.getElementById('chat-box');

    // Toggle para abrir e fechar
    chat.classList.toggle('active');
    
    // Se o chat for fechado, limpe o conteúdo e mostre apenas o menu
    if (!chat.classList.contains('active')) {
        chatBox.innerHTML = '';        
        showMainMenu();
    }
}

// Função que adiciona as mensagens no chat
function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);

    if (typeof message === 'string') {
        messageDiv.innerHTML = `
            <div class="profile"></div>
            <div class="msg"><p>${message}</p></div>
        `;
    }

    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; 
}

// Variável para armazenar a escolha do usuário
let currentChoice = null;
let isProcessing = false; 

// Função que envia a mensagem e interage com o backend
function sendMessage(message) {
    if (isProcessing) return; 
    isProcessing = true;

    appendMessage('user', `Você escolheu: ${message}`);

    if (currentChoice === '2') {
        
        if (message === '1') {
            appendMessage('bot', "Você escolheu a opção: Dicas de Planejamento Financeiro");
            message = "1-1";
        } else if (message === '2') {
            appendMessage('bot', "Você escolheu a opção: Dicas para Reduzir Dívidas");
            message = "1-2";
        } else if (message === '3') {
            appendMessage('bot', "Você escolheu a opção: Dicas para Poupar e Investir");
            message = "1-3";
        } else if (message === '4') {
            appendMessage('bot', "Você escolheu a opção: Dicas de Consumo Consciente");
            message = "1-4";
        } else if (message === '5') {
            appendMessage('bot', "Você escolheu a opção: Dicas de Crédito");
            message = "1-5";
        } else {
            appendMessage('bot', "Opção inválida, por favor escolha uma opção válida.");
            isProcessing = false;
            return;
        }
    }

    // Envia a mensagem para o backend
    fetch('/chat-response/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCsrfToken(),
        },
        body: `message=${message}`,
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('bot', data.response);

        // Se foi a opção "Assistente Financeiro", atualiza a escolha
        if (message === '2') {
            currentChoice = '2'; 
        } else {
            // Se não, volta ao menu principal
            showMainMenu();
        }
        isProcessing = false; 
    })
    .catch(error => {
        console.error('Erro:', error);
        appendMessage('bot', 'Desculpe, houve um erro. Tente novamente mais tarde.');
        isProcessing = false;
    });
}

// Função para mostrar o menu principal
function showMainMenu() {
    appendMessage('bot', "Escolha uma das opções abaixo para começar:\n1 - Consultar CPF\n2 - Assistente Financeiro");
    currentChoice = null; 
}

// Função para enviar mensagem do campo de input
function sendMessageFromInput() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();
    if (message) {
        sendMessage(message);
        userInput.value = ''; 
    }
}

// Função para lidar com a tecla Enter
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessageFromInput();
    }
}

// Função para obter o token CSRF do Django
function getCsrfToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}

// Função para reiniciar o chat com o menu inicial
function resetChat() {
    showMainMenu();
}

// Quando a página for carregada, inicializa o chat e adiciona os eventos
window.onload = function() {
    document.addEventListener('DOMContentLoaded', () => {
        resetChat(); 

        // Seleciona elementos do DOM
        const userInput = document.getElementById('user-input');
        const sendButton = document.querySelector('.footer button');

        // Adiciona os eventos aos elementos
        if (userInput && sendButton) {
            userInput.addEventListener('keypress', handleKeyPress);
            sendButton.addEventListener('click', sendMessageFromInput);
        }
    });
};
