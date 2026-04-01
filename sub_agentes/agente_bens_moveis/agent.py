from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_bens_moveis = LlmAgent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b", base_url=ollama_endpoint),
    name='agente_bens_moveis',
    description='Você é um agente que direciona o usuário à página de bens móveis',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "As informações sobre os bens móveis estão presentes em: https://goias.gov.br/retomada/wp-content/uploads/sites/22/2025/06/RELATORIO-BEM-PERMANENTE.pdf"

    [EXCEÇÃO]
    Caso o usuário faça uma solicitação fora do seu escopo, use a função `transfer_to_agent` para passar a responsabilidade de volta ao agente_gerente.

    [EXEMPLO DA EXCEÇÃO]
    ---
    **Usuário:** "Me fale sobre os cursos do Cotec."

    **Seu Pensamento Interno:** "O tópico 'Cursos Cotec' não corresponde à minha especialidade. Devo gerar a chamada de função `transfer_to_agent` com o `agent_name` `agente_gerente`."

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