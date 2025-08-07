document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const userInputForm = document.getElementById('user-input-form');
    const userInputField = document.getElementById('user-input');
})

userInputForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const userInput = userInputField.value;
    userInputField.value = '';

    appendMessage('user', userInput);
    
    const chatGPTResponse = getChatGPTResponse(userInput);

    appendMessage('chatbot', chatGPTResponse);    
});

function appendMessage(role, content) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);
    messageDiv.textContent = content;
    chatContainer.appendChild(messageDiv);
}

function getChatGPTResponse(userInput) {
    const response = fetch('/api/chat', {
        
    })
}



// const inputForm = document.getElementById('user-input-form').addEventListener('click', )