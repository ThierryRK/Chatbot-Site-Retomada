from google.adk.agents import SequentialAgent

from sub_agentes.agente_sequencia_doacoes.sub_agentes_sequencia.agente_de_resumos.agent import agente_de_resumos
from sub_agentes.agente_sequencia_doacoes.sub_agentes_sequencia.agente_extrator_de_conteudo_pagina_web.agent import \
    agente_extrator_de_conteudo_pagina_web

agente_sequencia_doacoes = SequentialAgent(
    name="agente_sequencia_doacoes",
    sub_agents=[agente_extrator_de_conteudo_pagina_web, agente_de_resumos],
    description="Sequencia que informa o usuário sobre as doações recebidas pelo orgão."
)