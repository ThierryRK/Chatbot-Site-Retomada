from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re

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
        res = requests.post(url_run, json=payload, timeout=1200)

        # 2. Se a sessão não existir (404), vamos criá-la
        if res.status_code == 404:
            print("Criando sessão...")
            url_session = f"{ADK_BASE_URL}/apps/{APP_NAME}/users/{user_id}/sessions/{session_id}"
            requests.post(url_session)  # Cria a sessão
            res = requests.post(url_run, json=payload)  # Tenta de novo

        if res.status_code == 200:
            data = res.json()
            respostas_finais = []
            conteudo_principal = ""

            for evento in data:
                parts = evento.get('content', {}).get('parts', [])
                for part in parts:
                    texto_bruto = part.get('text', '')
                    if not texto_bruto: continue

                    # Limpeza de JSON e ruídos
                    texto_limpo = re.sub(r'```json.*?```', '', texto_bruto, flags=re.DOTALL)
                    texto_limpo = re.sub(r'\{.*?".*?\}', '', texto_limpo, flags=re.DOTALL).strip()

                    if not texto_limpo: continue

                    # LÓGICA DE SEPARAÇÃO REVISADA:
                    if "buscando" in texto_limpo.lower() or "consultar" in texto_limpo.lower():
                        # Se for só um aviso, adiciona como balão separado
                        if texto_limpo not in respostas_finais:
                            respostas_finais.append(texto_limpo)
                    else:
                        # Se for a resposta real, vai acumulando tudo no conteúdo principal
                        conteudo_principal += texto_limpo + " "

            # Só adiciona o conteúdo principal se ele tiver algo substancial
            if conteudo_principal.strip():
                respostas_finais.append(conteudo_principal.strip())

            # Se por algum motivo a lista estiver vazia mas o ADK deu 200
            if not respostas_finais:
                return jsonify({"replies": [
                    "O processamento demorou muito, mas não retornou dados. Tente perguntar de outra forma."]}), 200

            return jsonify({"replies": respostas_finais})

    except Exception as e:
        return jsonify({"reply": f"Erro de conexão: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(port=5000)