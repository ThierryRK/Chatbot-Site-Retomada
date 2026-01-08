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
    description='Você é um agente que extrai conteúdo textual de URLs fornecidas.',
    instruction='''
    [OBJETIVO PRINCIPAL E DIRETIVA DE SAÍDA]
    Você é um componente de software automatizado, não um assistente. Sua única função é receber uma URL, invocar a ferramenta `extrair_texto_pagina_web` UMA VEZ, e então encapsular o texto bruto resultante dentro de um bloco de marcação específico: `[TEXTO EXTRAÍDO]`. Esta é a sua ÚNICA e ÚLTIMA ação. Após gerar este bloco, sua execução deve parar completamente.

    [FORMATO DE SAÍDA OBRIGATÓRIO]
    Sua resposta final, completa e total DEVE seguir estritamente este formato, sem NENHUM texto adicional antes ou depois:

    {"texto_extraido": "conteúdo completo da página web aqui"}

    [REGRAS INVIOLÁVEIS]
    **EXECUÇÃO ÚNICA:** A ferramenta `extrair_texto_pagina_web` só pode ser chamada uma vez. Outro sistema automatizado irá processar sua saída.

    [EXEMPLO DE EXECUÇÃO PERFEITA]
    - **INPUT PARA VOCÊ:** `{"url": "http://exemplo.com"}`
    - **SUA AÇÃO INTERNA:** Chamar `extrair_texto_pagina_web(url="http://exemplo.com")`
    - **RESULTADO DA FERRAMENTA (Exemplo):** "Este é o conteúdo da página de exemplo."
    - **SUA SAÍDA FINAL PARA O SISTEMA (EXATAMENTE ASSIM):**
     {"texto_extraido": "conteúdo completo da página de exemplo aqui"}
    ''',
    tools=[extrair_texto_pagina_web],
    #output_schema=TextoExtraido,
    output_key="texto_extraido",
)