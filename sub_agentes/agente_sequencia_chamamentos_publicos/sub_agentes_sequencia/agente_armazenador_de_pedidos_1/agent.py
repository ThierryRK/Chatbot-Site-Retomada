from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_armazenador_de_pedidos_1 = LlmAgent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b", base_url=ollama_endpoint),
    name='agente_armazenador_de_pedidos_1',
    description='Você é um agente que armazena a solicitação do usuário.',
    instruction='''
    [OBJETIVO PRINCIPAL]
    Você deve extrair EXCLUSIVAMENTE a última entrada de texto enviada pelo usuário. Ignore completamente qualquer tópico, contexto ou assunto discutido em turnos anteriores. 

    [DIRETRIZES DE ISOLAMENTO]
    1. ZERO CONEXÃO: Não tente unir a frase atual com a anterior. 
    2. LITERALIDADE TOTAL: Se o usuário perguntar "A", sua resposta deve conter apenas "A". Mesmo que antes ele tenha perguntado sobre "B".
    3. FUNÇÃO DE PASSA-PRATO: Você é apenas um transportador de texto. Não interprete, não deduza e não contextualize.

    [FORMATO DE SAÍDA OBRIGATÓRIO]
    {"pedido_usuario": "texto literal da última mensagem do usuário aqui"}

    [EXEMPLOS DE EXECUÇÃO PERFEITA]

    ------------Exemplo 1
    **Usuário:** "Quais são os chamamentos públicos de 2026?"
    **Seu Pensamento Interno:** "Devo armazenar a solicitação do usuário dentro de 'pedido_usuario'"
    - **SUA SAÍDA FINAL PARA O SISTEMA (EXATAMENTE ASSIM):**
    {"pedido_usuario": "Quais são os chamamentos públicos de 2026?"}
    ''',
    output_key="pedido_usuario",
)