lucide.createIcons();

var buttonChatbot = document.querySelector('.icon-chat'),
chat = document.querySelector('.chat'),
btnFechaChat = document.getElementById('botao-fechar');

btnFechaChat.addEventListener('click', () => {
    buttonChatbot.click();
})

buttonChatbot.addEventListener('click', () => {
    chat.classList.toggle('active');
})
