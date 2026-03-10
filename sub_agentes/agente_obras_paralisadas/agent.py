from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_obras_paralisadas = LlmAgent(
    model=LiteLlm(
        model="ollama_chat/ministral-3:14b",
        base_url=ollama_endpoint,
        # Adicione as linhas abaixo para controlar a VRAM
        completion_args={
            "options": {
                "num_ctx": 8192  # Limita o contexto a 8k tokens, economizando sua GPU
            }
        }
    ),
    name='agente_obras_paralisadas',
    description='Você é um agente que direciona o usuário à página de acordos de obras paralisadas',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "As informações sobre as obras paralisadas estão presentes em: https://app.powerbi.com/view?r=eyJrIjoiZjdhNDMxYjQtNDg3ZC00NjQ1LWI5M2EtMGRhMzg2OTNmMWZhIiwidCI6IjY3ZmQ0MzFjLWIyYWQtNDg2Ny04MWJjLWQ3NTYyMjBiNTZkNCJ9&pageName=ReportSection8f435ccde7de8820eb54"

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