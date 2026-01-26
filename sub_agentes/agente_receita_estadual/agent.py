from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_receita_estadual = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_receita_estadual',
    description='Você é um agente que direciona o usuário ao site da receita',
    instruction='''
    Sua única tarefa é:
    1. Responder a seguinte frase ao usuário:
    "Informações sobre a receita estadual presentes em: https://www.transparencia.go.gov.br/wp-content/uploads/sites/2/painel/lai.php?painel=receitas_estaduais&orgao=ser"
    ''',
)