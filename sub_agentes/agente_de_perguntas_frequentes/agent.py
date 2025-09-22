from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_de_perguntas_frequentes = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente de perguntas frequentes',
    description='Você é um agente que responde perguntas frequentes.',
    instruction='''
    Você é um assistente de perguntas frequentes sobre serviços oferecidos

    Quando perguntado sobre O Programa Mais Empregos responda que:
    
        Quem pode utilizar este serviço?

        Beneficiários do seguro-desemprego;
        Trabalhadores desempregados cadastrados no banco de dados do SINE;
        Trabalhadores empregados e desempregados afetados por processo de modernização tecnológica, choques comerciais e /oi outras formas de reestruturação econômica produtiva
        Beneficiários de políticas de inclusão social e de políticas de integração e desenvolvimento regional e local;
        Trabalhadores resgatados de regime de trabalho forçado ou reduzido a à condição análoga de escravo;
        Trabalhadores cooperativados, em condição associativa ou auto-gestionada, e empreendedores individuais;
        aprendizes;
        pessoas com deficiência (desde que observados o descrito no Art. 5º da Norma de Execução 113, de 14 de outubro de 2019/MTE);
        pessoas idosas.

        Área Responsável

            – Superintendência do Mais Empregos.

            – Gerência de intermediação e Recolocação do Trabalho.
        Legislação

            – LEI Nº 13.667, DE 17 DE MAIO DE 2018.

            – RESOLUÇÃO Nº 825, DE 26 DE MARÇO DE 2019

            – RESOLUÇÃO CODEFAT N.º 827 de 26.03.2019
    ''',
    sub_agents=[]
)
