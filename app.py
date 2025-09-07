# app.py
import os
import re
from flask import Flask, render_template, request, jsonify
import textwrap
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# --- Configuração da API do Gemini ---
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
except AttributeError:
    print("Erro: A chave de API do Google não foi encontrada.")
    exit()

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# --- INSTRUÇÕES E PERSONALIDADE DO BOT (PROMPT) ---
# Separado para ficar mais organizado
system_prompt = """
Você é um assistente virtual de atendimento ao cliente da empresa 'Soluções Inteligentes'. 
Seu nome é Vetric. 

**Sua Personalidade:**
- Seja sempre educado, prestativo e amigável. Use emojis para deixar a conversa mais leve.
- Responda de forma clara e objetiva.

**Informações sobre a Empresa e Produtos:**
- **Empresa:** Soluções Inteligentes, líder em software customizado.
- **Produto A - 'Connecta E-commerce':** Uma plataforma completa para lojas virtuais. Destaques: integração com redes sociais, cálculo de frete automático e painel de análise de vendas.
- **Produto B - 'Gestor Pro':** Um sistema de gestão interna (ERP) para pequenas e médias empresas. Destaques: controle de estoque, emissão de notas fiscais e gerenciamento de fluxo de caixa.
- **Contato:** Para falar com um vendedor, o cliente deve ligar para (11) 99999-8888 ou enviar um email para contato@solucoesinteligentes.dev.

**Regras:**
- **NUNCA** invente informações. Se você receber um "Contexto Interno:", baseie sua resposta PRIMEIRO nele.
- Se não souber a resposta, peça desculpas e indique os canais de contato humano.
- Use formatação Markdown (negrito `**texto**`, listas com `-`) para organizar as respostas.
"""

# Inicia a conversa com a instrução do sistema
convo = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]},
   
    {"role": "model", "parts": ["Olá! 👋 Eu sou o Vetric, o assistente virtual da Soluções Inteligentes. Como posso te ajudar a conhecer nossas soluções de software hoje?"]}
])


# --- (NOVO) SIMULAÇÃO DE UMA BASE DE DADOS INTERNA ---
def buscar_dados_empresa(query_usuario):
    """
    Esta função simula uma busca em um banco de dados ou API interna.
    Se encontrar uma informação relevante, retorna. Senão, retorna None.
    """
    query_lower = query_usuario.lower()
    
    # Exemplo: busca por palavras-chave relacionadas a preço
    if re.search(r'preço|valor|custo.*gestor pro', query_lower):
        return "O produto **Gestor Pro** tem um plano inicial de R$ 299,00 por mês. Para um orçamento detalhado, o ideal é falar com um de nossos especialistas."
    
    if re.search(r'preço|valor|custo.*connecta', query_lower):
        return "O preço da plataforma **Connecta E-commerce** varia conforme o projeto. Nosso time de vendas pode fornecer uma cotação precisa."

    # Se não encontrar nada específico, retorna None
    return None

# --- ROTAS DA APLICAÇÃO ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Mensagem vazia"}), 400

    try:
        # --- (NOVO) LÓGICA DE TRANSBORDO HUMANO ---
        if re.search(r'falar com.*atendente|humano|pessoa real', user_message.lower()):
            response_text =textwrap.dedent("""
            Claro! Para falar com um de nossos especialistas, você pode:
            - Ligar para **(11) 99999-8888**
            - Enviar um email para **contato@solucoesinteligentes.dev**
            Nosso horário de atendimento é de segunda a sexta, das 9h às 18h. 😉
            """)
            return jsonify({"response": response_text})

       
        dados_internos = buscar_dados_empresa(user_message)
        
        final_prompt = user_message
        if dados_internos:
            print(f"[LOG] Dados internos encontrados: {dados_internos}")
          
            final_prompt = f"Use este contexto interno para responder à pergunta do usuário.\nContexto Interno: '{dados_internos}'\n\nPergunta do Usuário: '{user_message}'"
        
        
        convo.send_message(final_prompt)
        bot_response = convo.last.text
        return jsonify({"response": bot_response})

    except Exception as e:
        print(f"ERRO DETALHADO: {e}")
        return jsonify({"error": f"Ocorreu um erro: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)