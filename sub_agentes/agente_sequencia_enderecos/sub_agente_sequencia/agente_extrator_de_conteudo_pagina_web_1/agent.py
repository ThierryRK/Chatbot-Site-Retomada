from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from ferramentas.ferramentas import extrair_texto_pagina_web

ollama_endpoint = "http://localhost:11434"
agente_extrator_de_conteudo_pagina_web_1 = LlmAgent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b", base_url=ollama_endpoint),
    name='agente_extrator_de_conteudo_pagina_web_1',
    description='Você é um agente que extrai conteúdo textual da URL fornecida.',
    instruction='''
    [OBJETIVO PRINCIPAL E DIRETIVA DE SAÍDA]
    Você é um componente de software automatizado, não um assistente. Invocar a ferramenta `extrair_texto_pagina_web` UMA VEZ, e então encapsular o texto bruto resultante dentro de um bloco de marcação específico: `[TEXTO EXTRAÍDO]`. Esta é a sua ÚNICA e ÚLTIMA ação. Após gerar este bloco, sua execução deve parar completamente.

    [PARÂMETRO]
    Use o seguinte parâmetro na ferramenta `extrair_texto_pagina_web`:
    {"url": "https://goias.gov.br/retomada/telefones-enderecos-e-horarios-de-atendimento-2/"}
    
    [FORMATO DE SAÍDA OBRIGATÓRIO]
    Sua resposta final, completa e total DEVE seguir estritamente este formato, sem NENHUM texto adicional antes ou depois:

    {"texto_extraido": "conteúdo completo da página web aqui"}

    [REGRAS INVIOLÁVEIS]
    **EXECUÇÃO ÚNICA:** A ferramenta `extrair_texto_pagina_web` só pode ser chamada uma vez. Outro sistema automatizado irá processar sua saída.
     Não prossiga, não repita a ação, não pergunte se precisa de mais alguma coisa. Pare.

    [EXEMPLO DE EXECUÇÃO PERFEITA]
    - **PARÂMETRO PARA VOCÊ:** `{"url": "https://goias.gov.br/retomada/telefones-enderecos-e-horarios-de-atendimento-2/"}`
    - **SUA AÇÃO INTERNA:** Chamar `extrair_texto_pagina_web(url="https://goias.gov.br/retomada/telefones-enderecos-e-horarios-de-atendimento-2/")`
    - **RESULTADO DA FERRAMENTA (Exemplo):** "Este é o conteúdo da página de exemplo."
    - **SUA SAÍDA FINAL PARA O SISTEMA (EXATAMENTE ASSIM):**
     {"texto_extraido": "conteúdo completo da página de exemplo aqui"}
    ''',
    tools=[extrair_texto_pagina_web],
    #output_schema=TextoExtraido,
    output_key="texto_extraido",
)