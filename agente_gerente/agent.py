from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from sub_agentes.agente_de_sequencia_de_resumos_de_pagina_web.agent import agente_de_sequencia_de_resumos_de_pagina_web

ollama_endpoint = "http://localhost:11434"
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='Gerente',
    description='Você é um agente que delega tarefas.',
    instruction='''
    Você é um agente gerente responsável por supervisionar o trabalho de outros agentes.

    Sempre encarregue a tarefa para os agente apropriados. Use o melhor do seu julgamento para determinar qual o agente apropriado para a tarefa.

    Você é responsável por encarregar tarefas para os seguintes agentes:
    - agente_de_sequencia_de_resumos_de_pagina_web
    
    Caso o usuário pergunte sobre o Programa Mais empregos, Cursos oferecidos pelo Cotec ou a Cerveja de mandioca passe delegue para a agente_de_sequencia_de_resumos_de_pagina_web
    
    Se o usúario não der informações o suficiente para decidir a quem delegar, peça ao usuário por mais informações.
    ''',
    sub_agents=[agente_de_sequencia_de_resumos_de_pagina_web]
)