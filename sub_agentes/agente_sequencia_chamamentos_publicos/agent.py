from google.adk.agents import SequentialAgent

from sub_agentes.agente_sequencia_chamamentos_publicos.sub_agentes_sequencia.agente_armazenador_de_pedidos_1.agent import \
    agente_armazenador_de_pedidos_1
from sub_agentes.agente_sequencia_chamamentos_publicos.sub_agentes_sequencia.agente_chamamentos_publicos.agent import \
    agente_chamamentos_publicos
from sub_agentes.agente_sequencia_chamamentos_publicos.sub_agentes_sequencia.agente_extrator_de_conteudo_pagina_web_3.agent import \
    agente_extrator_de_conteudo_pagina_web_3

agente_sequencia_chamamentos_publicos = SequentialAgent(
    name="agente_sequencia_chamamentos_publicos",
    sub_agents=[agente_armazenador_de_pedidos_1, agente_extrator_de_conteudo_pagina_web_3, agente_chamamentos_publicos],
    description="Sequencia que informa o usuário sobre os chamamentos públicos do orgão."
)