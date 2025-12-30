from google.adk.agents import SequentialAgent

from sub_agentes.agente_sequencia_comunicacao.sub_agente_sequencia import agente_selecionador_meio_comunicacao
from sub_agentes.agente_sequencia_comunicacao.sub_agente_sequencia import agente_extrator_de_conteudo_pagina_web
from sub_agentes.agente_sequencia_comunicacao.sub_agente_sequencia import agente_armazenador_de_pedidos

agente_sequencia_comunicacao = SequentialAgent(
    name="agente_sequencia_comunicacao",
    sub_agents=[agente_armazenador_de_pedidos, agente_extrator_de_conteudo_pagina_web, agente_selecionador_meio_comunicacao],
    description="Sequencia que extraí o conteúdo de página web e então responde meios de comunicação baseados na solicitação do usuário."
)