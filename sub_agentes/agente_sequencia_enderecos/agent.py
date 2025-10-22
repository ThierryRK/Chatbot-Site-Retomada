from google.adk.agents import SequentialAgent

agente_sequencia_enderecos = SequentialAgent(
    name="agente_sequencia_enderecos",
    sub_agents=[],
    description="Sequencia que extraí o conteúdo de página web e então responde enderecos baseados na solicitação do usuário."
)