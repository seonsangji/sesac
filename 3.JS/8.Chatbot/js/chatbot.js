document.addEventListener('DOMContentLoaded', initChatbot);

function initChatbot() {
    createChatbotUI();
    registerEventHandlers();
    enableResize();
}

function createChatbotUI() {
    const chatbotHTML = `
        <div class="chatbot-icon" id="chatbotIcon">
            <i class="bi bi-chat-dtos-fill icon-back"></i>
            <i class="bi bi-chat-heart icon-front"></i>
        </div>

        <div class="chatbot-window" id="chatbotWindow">
            <div class="chatbot-header">
                <span>Chatbot</span>
                <button id="closeChatbot">X</button>
            </div>
            <div class="chatbot-body">
                <div class="chatbot-messages" id="chatbotMessages"></div>
                <div class="chatbot-input-container">
                    <input type="text" id="chatbotInput" placeholder="Type a message">
                    <button id="sendMessage">send</button>
                </div>
            </div>
            <div class="resizer"></div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', chatbotHTML)
}

function registerEventHandlers() {
    const chatbotIcon = document.getElementById('chatbotIcon');
    const chatbotWindow = document.getElementById('chatbotWindow');
    const closeChatbot = document.getElementById('closeChatbot');
    const sendMessage = document.getElementById('sendMessage');
    const chatbotInput = document.getElementById('chatbotInput');

    chatbotIcon.addEventListener('click', () => {
        chatbotIcon.style.display = 'none';
        chatbotWindow.style.display = 'flex';
    })

    closeChatbot.addEventListener('click', () =>{
        chatbotWindow.style.display = 'none';
        chatbotIcon.style.display = 'flex'
    });

    sendMessage.addEventListener('click', handleUserMessage);
    chatbotInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleUserMessage();
    })
}

function enableResize() {
    const resizer = document.querySelector('.resizer');
    const chatbotWindow = document.getElementById('chatbotWindow');
    let isResizing = false;
    let startX, startY, startWidth, startHeight;

    resizer.addEventListener('mousedown', function (e) {
        isResizing = true;
        startX = e.clientX;
        startY = e.clientY;
        startWidth = chatbotWindow.offsetWidth;
        startHeight = chatbotWindow.offsetHeight;
        document.body.style.userSelect = 'none';

        function doResize(e) {
            if (!isResizing) return;
            // 얼마나 움직였는지
            const dx = startX - e.clientX;
            const dy = startY - e.clientY;
            // width/height 늘림 (최소값 고려)
            chatbotWindow.style.width = Math.max(300, Math.min(startWidth + dx,600)) + 'px';
            chatbotWindow.style.height = Math.max(400, Math.min(startHeight + dy,800)) + 'px';
        }

        function stopResize() {
            isResizing = false;
            document.body.style.userSelect = '';
            window.removeEventListener('mousemove', doResize);
            window.removeEventListener('mouseup', stopResize);
        }

        window.addEventListener('mousemove', doResize);
        window.addEventListener('mouseup', stopResize);
    });
}



async function handleUserMessage() {
    const input = document.getElementById('chatbotInput')
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, 'user');
    const botResponse = '[BOT] ' + input.value;
    input.value = '';

    addMessage(botResponse, 'bot')
}

function addMessage(message, sender) {
    const container = document.getElementById('chatbotMessages');
    // const formatted = message

    const messageElement = document.createElement('div')
    messageElement.innerHTML = sender === 'user'
        ? `<i class="bi bi-person"></i> ${message}`
        : `<i class="bi bi-robot"></i> ${message}`
    messageElement.classList.add(sender);

    container.appendChild(messageElement);
    container.scrollTop = container.scrollHeight;
}


const ECHO_MODE = true;

async function sendMessageToServer(user_input) {
    if (ECHO_MODE) {
        return `Echo: ${user_input}`
    }
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body : JSON.stringify({user_input})
    });
    const data = await response.json();
    return data.chatbot
}
