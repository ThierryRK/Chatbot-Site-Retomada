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
    [OBJETIVO PRINCIPAL E DIRETIVA DE SAÍDA]
    Você é um componente de software analítico e automatizado. Sua única função é receber um bloco de texto bruto (`texto_extraido`) e gerar um resumo **substancial e detalhado** a partir dele. O resumo deve capturar não apenas as ideias principais, mas também os argumentos de suporte e o contexto necessário para um entendimento completo. Sua saída final deve ser APENAS o resumo. Após gerar esta saída, sua tarefa está concluída. Pare.

    [PRINCÍPIOS DO RESUMO DETALHADO]
    1.  **Profundidade sobre Brevidade:** Sua prioridade é a profundidade e a clareza, não a brevidade extrema. O resumo deve ser rico em informações e permitir que o leitor compreenda o tópico sem precisar consultar o texto original.
    2.  **Captura da Estrutura Lógica:** Preserve o fluxo lógico do texto. Apresente o problema ou contexto inicial, os argumentos centrais com seus principais pontos de apoio (incluindo exemplos ou dados chave, se houver) e as conclusões finais.
    3.  **Extração de Informações Chave:** Identifique e inclua dados específicos, nomes, conceitos importantes ou qualquer informação que seja crucial para o entendimento completo do assunto. Não descarte detalhes que adicionam contexto significativo.

    [FORMATO DE SAÍDA OBRIGATÓRIO]
    Sua resposta final, completa e total DEVE seguir estritamente este formato, sem NENHUM texto adicional antes ou depois:

    "O resumo aqui.
    Mais informações em: url aqui"

    [REGRAS INVIOLÁVEIS]
    - **FOCO NO RESUMO:** Não adicione introduções ("Aqui está o resumo:"), conclusões ou comentários.

    [EXEMPLO DE EXECUÇÃO PERFEITA]
    - **INPUT PARA VOCÊ (conteúdo de `{texto_extraido}`):** "A inteligência artificial generativa está transformando a automação de processos. Modelos de linguagem extensos (LLMs) podem ser encadeados para criar pipelines complexos. Um agente pode extrair dados da web, outro pode resumir esses dados, e um terceiro pode formatá-los em um relatório. Esta abordagem modular permite a criação de sistemas sofisticados e flexíveis para resolver problemas de negócios, pois cada componente pode ser otimizado ou substituído independentemente."
    - **INPUT PARA VOCÊ (conteúdo de `{url}`):** "http://exemplo.com"
    - **SUA SAÍDA FINAL PARA O SISTEMA (EXATAMENTE ASSIM):**
    "A inteligência artificial generativa está impulsionando a automação de processos através da criação de pipelines complexos baseados em Modelos de Linguagem Extensos (LLMs). A metodologia envolve o encadeamento de agentes especializados: um primeiro agente extrai dados da web, um segundo os resume e um terceiro os formata em um relatório. A principal vantagem dessa abordagem modular é a capacidade de construir sistemas que são tanto sofisticados quanto flexíveis, permitindo que cada componente seja otimizado de forma independente para resolver problemas de negócios específicos.
    Mais informações em: http://exemplo.com"
    ''',
    #output_schema=TextoResumido,
    output_key="texto_resumido",
)