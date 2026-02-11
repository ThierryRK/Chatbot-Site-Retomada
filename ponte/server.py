from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Libera o acesso para o seu HTML de teste e WordPress

ADK_BASE_URL = "http://127.0.0.1:8000"
APP_NAME = "agente_gerente"  # <--- O nome exato que o seu curl retornou!
USER_ID = "usuario_web_01"
SESSION_ID = "sessao_site_retomada"


@app.route('/chat', methods=['POST'])
def chat():
    user_text = request.json.get('message')
    user_id = "1"
    session_id = "sessao_fixa_01"

    # 1. Tenta rodar o agente
    url_run = f"{ADK_BASE_URL}/run"
    payload = {
        "appName": APP_NAME,
        "userId": user_id,
        "sessionId": session_id,
        "newMessage": {"parts": [{"text": user_text}], "role": "user"},
        "streaming": False
    }

    try:
        res = requests.post(url_run, json=payload)

        # 2. Se a sessão não existir (404), vamos criá-la
        if res.status_code == 404:
            print("Criando sessão...")
            url_session = f"{ADK_BASE_URL}/apps/{APP_NAME}/users/{user_id}/sessions/{session_id}"
            requests.post(url_session)  # Cria a sessão
            res = requests.post(url_run, json=payload)  # Tenta de novo

        if res.status_code == 200:
            data = res.json()
            # Extração segura da resposta
            reply = data[0]['content']['parts'][0]['text']
            return jsonify({"reply": reply})
        else:
            return jsonify({"reply": f"Erro no ADK: {res.status_code}"})

    except Exception as e:
        return jsonify({"reply": f"Erro de conexão: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(port=5000)