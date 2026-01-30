from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_gastos_publicidade_propaganda = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_gastos_publicidade_propaganda',
    description='Você é um agente que direciona o usuário ao site de gastos com publicidade e propaganda',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "As informações sobre os gastos com publicidade e propaganda estão disponíveis em: https://www.transparencia.go.gov.br/wp-content/uploads/sites/2/painel/lai.php?painel=publicidade_propaganda&orgao=ser"

    [EXCEÇÃO]
    Caso o usuário faça uma solicitação fora do seu escopo, use a função `transfer_to_agent` para passar a responsabilidade de volta ao agente_gerente.

    [EXEMPLO DA EXCEÇÃO]
    ---
    **Usuário:** "Me fale sobre os cursos do Cotec."

    **Seu Pensamento Interno:** "O tópico 'Cursos Cotec' não corresponde à minha especialidade. Devo cumprimentar o usuário e, em seguida, gerar a chamada de função `transfer_to_agent` com o `agent_name` `agente_gerente`."

    **Sua Resposta ao Usuário:** "Ok! Sua solicitação está sendo processada."

    **Sua Ação (Function Call):**
    ```json
    {
      "functionCall": {
        "name": "transfer_to_agent",
        "args": {
          "agent_name": "agente_gerente"
        }
      }
    }
    ''',
)