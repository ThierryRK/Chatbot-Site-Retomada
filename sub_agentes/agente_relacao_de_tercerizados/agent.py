from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_relacao_de_tercerizados = LlmAgent(
    model=LiteLlm(
        model="ollama_chat/ministral-3:14b",
        base_url=ollama_endpoint,
        # Adicione as linhas abaixo para controlar a VRAM
        completion_args={
            "options": {
                "num_ctx": 8192  # Limita o contexto a 8k tokens, economizando sua GPU
            }
        }
    ),    name='agente_relacao_de_tercerizados',
    description='Você é um agente que direciona o usuário à página de relação de tercerizados',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "As informações sobre a relação de tercerizados estão presentes em: https://goias.gov.br/retomada/acordos-sem-transferencia-de-recursos/"

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