// static/script.js
document.addEventListener("DOMContentLoaded", () => {
    // Elementos da interface
    const chatContainer = document.getElementById("chat-container");
    const chatOpenBtn = document.getElementById("chat-open-btn");
    const closeChatBtn = document.getElementById("close-chat-btn");
    const newChatBtn = document.getElementById("new-chat-btn"); // (MUDANÇA) Botão de recomeçar
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const chatBox = document.getElementById("chat-box");
    let typingIndicator; // Será definido dentro do resetChat

    // --- (MUDANÇA) FUNÇÃO PARA RECOMEÇAR O CHAT ---
    const resetChat = () => {
        // Limpa o conteúdo do chat e o recria do zero
        chatBox.innerHTML = `
            <div class="message bot-message">
                <p>Olá! 👋 Eu sou o Vetric. Posso te ajudar com alguma dúvida sobre nossos produtos?</p>
            </div>
            <div class="suggestion-box">
                <button class="suggestion-btn">O que faz o Connecta E-commerce?</button>
                <button class="suggestion-btn">Qual o preço do Gestor Pro?</button>
                <button class="suggestion-btn">Falar com um atendente</button>
            </div>
            <div id="typing-indicator" class="message bot-message" style="display: none;">
                 <div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>
            </div>
        `;
        // Pega a referência para o novo indicador de "digitando"
        typingIndicator = document.getElementById("typing-indicator");
        // Reativa os botões de sugestão
        attachSuggestionListeners();
    };

    // --- (MUDANÇA) FUNÇÃO PARA ATIVAR AS SUGESTÕES ---
    const attachSuggestionListeners = () => {
        document.querySelectorAll('.suggestion-btn').forEach(button => {
            button.addEventListener('click', () => {
                const question = button.textContent;
                userInput.value = question;
                sendMessage();
            });
        });
    };

    // Lógica para abrir e fechar o chat
    chatOpenBtn.addEventListener('click', () => {
        chatContainer.classList.add('open');
        chatOpenBtn.style.opacity = '0';
    });
    closeChatBtn.addEventListener('click', () => {
        chatContainer.classList.remove('open');
        chatOpenBtn.style.opacity = '1';
    });
    
    // (MUDANÇA) Event listener para o botão de recomeçar
    newChatBtn.addEventListener('click', resetChat);

    // Função principal para enviar a mensagem
    const sendMessage = async () => {
        const messageText = userInput.value.trim();
        if (messageText === "") return;

        // Esconde as sugestões após a primeira mensagem
        const suggestionBox = document.querySelector('.suggestion-box');
        if (suggestionBox) {
            suggestionBox.style.display = 'none';
        }

        appendMessage(messageText, "user-message", true);
        userInput.value = "";
        typingIndicator.style.display = "flex";
        chatBox.scrollTop = chatBox.scrollHeight;

        try {
            const response = await fetch("/send_message", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: messageText }),
            });
            if (!response.ok) throw new Error("A resposta da rede não foi 'ok'.");
            const data = await response.json();
            appendMessage(data.response, "bot-message", false);
        } catch (error) {
            console.error("Erro ao enviar mensagem:", error);
            appendMessage("Desculpe, ocorreu um erro. Tente novamente mais tarde.", "bot-message", false);
        } finally {
            typingIndicator.style.display = "none";
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    };
    
    // Função para adicionar mensagens na tela
    const appendMessage = (text, className, isSimpleText) => {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", className);
        const p = document.createElement("p");
        if (isSimpleText) {
            p.textContent = text;
        } else {
            p.innerHTML = marked.parse(text);
        }
        messageDiv.appendChild(p);
        chatBox.insertBefore(messageDiv, typingIndicator);
        chatBox.scrollTop = chatBox.scrollHeight;
    };

    // Listeners do input e botão de enviar
    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (event) => {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    // (MUDANÇA) Inicia o chat pela primeira vez quando a página carrega
    resetChat();
});