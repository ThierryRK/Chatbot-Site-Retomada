from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from ferramentas.ferramentas import extrair_texto_pagina_web

ollama_endpoint = "http://localhost:11434"
agente_extrator_de_conteudo_pagina_web = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_extrator_de_conteudo_pagina_web',
    description='Você é um agente que extraí textos de páginas web.',
    instruction='''
    Você é um agente que extraí textos de páginas web.
    
    Use o url recebido para extrair e armazenar o conteúdo da página web.
    ''',
    tools=[extrair_texto_pagina_web]
)