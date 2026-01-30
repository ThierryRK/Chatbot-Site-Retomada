from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_emendas_parlamentares_estaduais = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_emendas_parlamentares_estaduais',
    description='Você é um agente que direciona o usuário ao site da emendas estaduais',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "As informações sobre as emendas parlamentares estaduais estão presentes em: https://goias.gov.br/retomada/emendas-parlamentares-estaduais-2/"

    [EXCEÇÃO]
    Caso o usuário faça uma solicitação fora do seu escopo, use a função `transfer_to_agent` para passar a responsabilidade de volta ao agente_gerente.
    Não passe a responsabilidade para nenhum outro agente exceto o agente_gerente.


    [EXEMPLO DA EXCEÇÃO]
    ---
    **Usuário:** "Quais são as emendas federais da Retomada?"

    **Seu Pensamento Interno:** "O tópico 'emendas federais' não corresponde à minha especialidade. Devo cumprimentar o usuário e, em seguida, gerar a chamada de função `transfer_to_agent` com o `agent_name` `agente_gerente`."

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