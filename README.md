# Vetric - Chatbot with Python and Google API

![Demonstração do Chatbot Vetric](demo.gif)

### 🌐 [Try the live demo here!](https://gustarlz.pythonanywhere.com/)

A simple assistant chatbot built as a practical exercise to learn Python, Flask, and integration with external APIs. This project serves as a functional test of these technologies working together.

---

<details open>
<summary><strong>𝗘𝗡 English Version</strong></summary>

### Project Context Note
To demonstrate the assistant's customization capabilities, it has been configured for a **fictional company ("Soluções Inteligentes") with fictional products**. The chatbot's name, "Vetric," and all product details mentioned in the conversation are part of this simulation to showcase a real-world use case.

### Features
- **Floating Widget Interface:** A chat window that can be opened and closed on any page.
- **Clickable Question Suggestions:** Buttons to help users start the conversation.
- **Conversation Reset Button:** Clears the chat history to start a new session.
- **AI-Powered Responses (via Google API):** Uses the Google API to generate conversational replies.
- **Markdown Formatting Support:** The bot's responses are rendered with basic formatting like bold text and lists.

### Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **API:** Google API
- **Python Libraries:** `google-generativeai`, `python-dotenv`

### How to Run Locally
1.  **Prerequisites:** Python 3.8+, Git
2.  **Clone:** `git clone https://github.com/gustarlz/YOUR-REPOSITORY-NAME.git && cd YOUR-REPOSITORY-NAME` <!--- PREENCHA AQUI -->
3.  **Environment:** `py -m venv venv && .\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
4.  **Install:** `pip install -r requirements.txt`
5.  **Configure:** Create a `.env` file and add `GOOGLE_API_KEY=YOUR_SECRET_API_KEY_HERE`
6.  **Run:** `py app.py` and navigate to `http://127.0.0.1:5000`.

---
*Developed by gustarlz.*

</details>

<br>

<details open>
<summary><strong>🇧🇷 Versão em Português</strong></summary>

### Nota sobre o Contexto do Projeto
Para demonstrar a capacidade de personalização do assistente, ele foi configurado para uma **empresa fictícia ("Soluções Inteligentes") com produtos também fictícios**. O nome do chatbot, "Vetric", e todos os detalhes de produtos mencionados na conversa fazem parte dessa simulação para apresentar um caso de uso prático.

### Funcionalidades
- **Interface de Widget Flutuante:** Uma janela de chat que pode ser aberta e fechada em qualquer página.
- **Sugestões de Perguntas Clicáveis:** Botões para ajudar o usuário a iniciar a conversa.
- **Botão para Recomeçar a Conversa:** Limpa o histórico do chat para iniciar uma nova sessão.
- **Respostas com IA (via Google API):** Utiliza a API do Google para gerar respostas conversacionais.
- **Suporte a Formatação Markdown:** As respostas do bot são renderizadas com formatação básica, como negrito e listas.

### Tecnologias Utilizadas
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **API:** Google API
- **Bibliotecas Python:** `google-generativeai`, `python-dotenv`

### Como Executar Localmente
1.  **Pré-requisitos:** Python 3.8+, Git
2.  **Clonar:** `git clone https://github.com/gustarlz/SEU-REPOSITORIO.git && cd SEU-REPOSITORIO` <!--- PREENCHA AQUI -->
3.  **Ambiente Virtual:** `py -m venv venv && .\venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (macOS/Linux)
4.  **Instalar:** `pip install -r requirements.txt`
5.  **Configurar:** Crie um arquivo `.env` e adicione `GOOGLE_API_KEY=SUA_CHAVE_DE_API_SECRETA_AQUI`
6.  **Executar:** `py app.py` e acesse `http://127.0.0.1:5000`.

---
*Desenvolvido por gustarlz.*

</details>
