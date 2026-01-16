from google.adk.agents import Agent, LlmAgent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field

from ferramentas.ferramentas import extrair_texto_pagina_web

#class TextoExtraido(BaseModel):
#    texto_extraido: str = Field(description="Texto extraído da página web")

ollama_endpoint = "http://localhost:11434"
agente_extrator_de_conteudo_pagina_web = LlmAgent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b", base_url=ollama_endpoint),
    name='agente_extrator_de_conteudo_pagina_web',
    description='Extrai texto de URLs e retorna JSON.',
    instruction='''
    Sua única tarefa é:
    1. Chamar a ferramenta `extrair_texto_pagina_web` usando a URL que você recebeu como entrada.
    2. Pegar o resultado bruto e retornar APENAS um JSON no formato: {"texto_extraido": "resultado da ferramenta"}
    3. Finalize IMEDIATAMENTE após emitir o JSON. Não adicione nenhum texto antes ou depois.
    ''',
    tools=[extrair_texto_pagina_web],
    #output_schema=TextoExtraido,
    output_key="texto_extraido",
)