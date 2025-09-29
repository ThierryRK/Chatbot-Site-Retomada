from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field


class URLEscolhido(BaseModel):
    url: str = Field(description="URL de uma página web.")

ollama_endpoint = "http://localhost:11434"
agente_selecionador_de_url = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_selecionador_de_url',
    description='Você é um agente que seleciona os url.',
    instruction='''
    Você é um agente que seleciona e armazena o url certo para ocasião baseado nas intruções a seguir:
    
    Caso o usuário deseje informações sobre o Programa Mais empregos escolha o seguinte url:
    https://goias.gov.br/retomada/perguntas-frequentes-sobre-o-programa-mais-empregos/
    
    Caso o usuário deseje informações sobre Cursos oferecidos pelo Cotec escolha o seguinte url:
    https://goias.gov.br/retomada/perguntas-frequentes-sobre-o-cursos-oferecidos-pelo-cotec/
    
    Caso o usuário deseje informações sobre a Cerveja de mandioca escolha o seguinte url:
    https://goias.gov.br/retomada/perguntas-frequentes-sobre-a-cerveja-de-mandioca/
    
    IMPORTANTE: a resposta deve se um JSON válido atendendo a seguinte estrutura:
    {"url": "url aqui"}
    
    NÃO inclua quaisquer explicações, texto adicional, espaços vazios ou quebras de linhas além da resposta JSON.
    ''',
    output_schema=URLEscolhido,
    output_key="url"
)