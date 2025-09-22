from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from sub_agentes.agente_de_perguntas_frequentes.agent import agente_de_perguntas_frequentes
from sub_agentes.agente_de_redirecionamento_de_páginas.agent import agente_de_redirecionamento_de_páginas
from sub_agentes.agente_de_tranferência_para_atendimento_humano.agent import \
    agente_de_tranferência_para_atendimento_humano

ollama_endpoint = "http://localhost:11434"
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='Gerente',
    description='Você é um agente que delega tarefas.',
    instruction='''
    Você é um agente gerente responsável por supervisionar o trabalho de outros agentes.

    Sempre encarregue a tarefa para os agente apropriados. Use o melhor do seu julgamento para determinar qual o agente apropriado para a tarefa.

    Você é responsável por encarregar tarefas para os seguintes agentes:
    - agente_de_perguntas_frequentes
    - agente_de_redirecionamento_de_páginas
    - agente_de_tranferência_para_atendimento_humano

    ''',
    sub_agents=[agente_de_perguntas_frequentes, agente_de_redirecionamento_de_páginas,
                agente_de_tranferência_para_atendimento_humano]
)