from google.adk.agents import SequentialAgent

from sub_agentes.agente_sequencia_meio_comunicacao.sub_agente_sequencia.agente_armazenador_de_pedidos_2.agent import \
    agente_armazenador_de_pedidos_2
from sub_agentes.agente_sequencia_meio_comunicacao.sub_agente_sequencia.agente_extrator_de_conteudo_pagina_web_4.agent import \
    agente_extrator_de_conteudo_pagina_web_4
from sub_agentes.agente_sequencia_meio_comunicacao.sub_agente_sequencia.agente_selecionador_comunicacao.agent import \
    agente_selecionador_comunicacao

agente_sequencia_meio_comunicacao = SequentialAgent(
    name="agente_sequencia_meio_comunicacao",
    sub_agents=[agente_armazenador_de_pedidos_2, agente_extrator_de_conteudo_pagina_web_4, agente_selecionador_comunicacao],
    description="Sequencia que extraí o conteúdo de página web e então responde meios de comunicação baseados na solicitação do usuário."
)