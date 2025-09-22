from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_de_tranferência_para_atendimento_humano = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente de tranferência para atendimento humano',
    description='Você é um agente que transfere o atendimento para um humano.',
    instruction='''
    você é um assistente que transfere o atendimento para um humano qunado necessário.

    ''',
    sub_agents=[]
)
