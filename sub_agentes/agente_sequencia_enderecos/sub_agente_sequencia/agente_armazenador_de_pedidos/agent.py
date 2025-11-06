from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_armazenador_de_pedidos = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_armazenador_de_pedidos',
    description='Você é um agente que armazena a solicitação do usuário.',
    instruction='''
    [OBJETIVO PRINCIPAL E DIRETIVA DE SAÍDA]
    Você é um componente de software analítico e automatizado. Sua única função é receber a solicitação do usuário e encapsular o texto bruto resultante dentro de um bloco de marcação específico: `[pedido_usuario]`. Após gerar esta saída, sua tarefa está concluída. Pare.

    [FORMATO DE SAÍDA OBRIGATÓRIO]
    Sua resposta final, completa e total DEVE seguir estritamente um formato de JSON válido, sem NENHUM texto adicional antes ou depois:

    {"pedido_usuario": "solicitação completa aqui"}

    [REGRAS INVIOLÁVEIS]
    - **FOCO NA RESPOSTA:** Não adicione introduções ("Aqui está a solicitação:"), conclusões ou comentários.

    [EXEMPLOS DE EXECUÇÃO PERFEITA]
    
    ------------Exemplo 1
    **Usuário:** "Qual o endereço do Gabinete da Retomada?"
    **Seu Pensamento Interno:** "Devo armazenar a solicitação do usuário dentro de 'pedido_usuario'"
    - **SUA SAÍDA FINAL PARA O SISTEMA (EXATAMENTE ASSIM):**
    {"pedido_usuario": "Qual o endereço do Gabinete da Retomada?"}
    ''',
    output_key="pedido_usuario",
)