from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from ferramentas.ferramentas import extrair_texto_pagina_web

ollama_endpoint = "http://localhost:11434"
agente_extrator_de_conteudo_pagina_web_4 = LlmAgent(
    model=LiteLlm(
        model="ollama_chat/ministral-3:14b",
        base_url=ollama_endpoint,
        # Adicione as linhas abaixo para controlar a VRAM
        completion_args={
            "options": {
                "num_ctx": 8192  # Limita o contexto a 8k tokens, economizando sua GPU
            }
        }
    ),    name='agente_extrator_de_conteudo_pagina_web_4',
    description='Você é um agente que extrai conteúdo textual da URL fornecida.',
    instruction='''
    Sua única tarefa é:
    1. Chamar a ferramenta `extrair_texto_pagina_web` para a URL: https://goias.gov.br/retomada/telefones-enderecos-e-horarios-de-atendimento-2/
    2. Pegar o resultado e retornar APENAS um JSON no formato: {"texto_extraido": "resultado da ferramenta"}
    3. Finalize após emitir o JSON.
    ''',
    tools=[extrair_texto_pagina_web],
    #output_schema=TextoExtraido,
    output_key="texto_extraido",
)