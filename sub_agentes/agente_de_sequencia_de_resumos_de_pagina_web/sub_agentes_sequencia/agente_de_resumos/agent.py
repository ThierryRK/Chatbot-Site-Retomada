from google.adk.agents import Agent, LlmAgent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field


#class TextoResumido(BaseModel):
#    texto_resumido: str = Field(description="Texto resumido da página web.")

ollama_endpoint = "http://localhost:11434"
agente_de_resumos = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_de_resumos',
    description='Você é um agente que resumi o texto recebido.',
    instruction='''
    Você é um agente que resumi o texto recebido enfatizando os pontos mais importantes para o conteúdo
    
    Resuma o texto extraido de maneira concisa, mas completa.
    
    **Conteúdo para resumir:**
    {texto_extraido}
    ''',
    #output_schema=TextoResumido,
    output_key="texto_resumido",
)