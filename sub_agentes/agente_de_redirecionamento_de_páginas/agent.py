from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_de_redirecionamento_de_páginas = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente de redirecionamento de páginas',
    description='Você é um agente que envia links de redirecionamento para páginas do site.',
    instruction='''
    Você é um assistente que envia links do site e dá uma breve descrição sobre o conteúdo.

    ''',
    sub_agents=[]
)
