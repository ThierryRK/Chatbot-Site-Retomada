from google.adk.agents import SequentialAgent

from sub_agentes.agente_sequencia_enderecos.sub_agente_sequencia.agente_armazenador_de_pedidos.agent import \
    agente_armazenador_de_pedidos
from sub_agentes.agente_sequencia_enderecos.sub_agente_sequencia.agente_extrator_de_conteudo_pagina_web_1.agent import \
    agente_extrator_de_conteudo_pagina_web_1
from sub_agentes.agente_sequencia_enderecos.sub_agente_sequencia.agente_selecionador_de_enderecos.agent import \
    agente_selecionador_enderecos

agente_sequencia_enderecos = SequentialAgent(
    name="agente_sequencia_enderecos",
    sub_agents=[agente_armazenador_de_pedidos, agente_extrator_de_conteudo_pagina_web_1, agente_selecionador_enderecos],
    description="Sequencia que extraí o conteúdo de página web e então responde enderecos baseados na solicitação do usuário."
)