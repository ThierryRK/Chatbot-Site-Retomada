from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_receita_estadual = LlmAgent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b", base_url=ollama_endpoint),
    name='agente_receita_estadual',
    description='Você é um agente que direciona o usuário ao site da receita',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "As informações sobre a receita estadual estão disponíveis em: https://www.transparencia.go.gov.br/wp-content/uploads/sites/2/painel/lai.php?painel=receitas_estaduais&orgao=ser"

    [EXCEÇÃO]
    Caso o usuário faça uma solicitação fora do seu escopo, use a função `transfer_to_agent` para passar a responsabilidade a outro agente.

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