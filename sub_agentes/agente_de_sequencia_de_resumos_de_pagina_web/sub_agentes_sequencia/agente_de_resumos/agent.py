from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_de_resumos = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_de_resumos',
    description='Você é um agente que resumi o texto recebido.',
    instruction='''
    Você é um agente que resumi o texto recebido enfatizando os pontos mais importantes para o conteúdo
    
    Resuma o texto extraido de maneira concisa, mas completa.
    ''',
)