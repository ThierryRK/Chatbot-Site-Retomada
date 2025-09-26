from google.adk.agents import SequentialAgent

from sub_agentes.agente_de_sequencia_de_resumos_de_pagina_web.sub_agentes_sequencia.agente_de_resumos.agent import \
    agente_de_resumos
from sub_agentes.agente_de_sequencia_de_resumos_de_pagina_web.sub_agentes_sequencia.agente_extrator_de_conteudo_pagina_web.agent import \
    agente_extrator_de_conteudo_pagina_web
from sub_agentes.agente_de_sequencia_de_resumos_de_pagina_web.sub_agentes_sequencia.agente_selecionador_de_url.agent import \
    agente_selecionador_de_url

agente_de_sequencia_de_resumos_de_pagina_web = SequentialAgent(
    name="agente_de_sequencia_de_resumos_de_pagina_web",
    sub_agents=[agente_selecionador_de_url, agente_extrator_de_conteudo_pagina_web, agente_de_resumos],
    description="Sequencia que escolhe o url, extraí conteúdo de página web e resume a informação coletada."
)
