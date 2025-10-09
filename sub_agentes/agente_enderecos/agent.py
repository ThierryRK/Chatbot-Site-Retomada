from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_endpoint = "http://localhost:11434"
agente_suporte_humano = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen2.5:14b", base_url=ollama_endpoint),
    name='agente_suporte_humano',
    description='Você é um agente que informa endereços ao usuário.',
    instruction='''
    Você é um agente que informa endereços ao usuário:

    Caso o usuário deseje saber a localização do Palácio Pedro Ludovico Texeira, responda essas informações:
    Rua 82, nº 400 Ed. Palácio Pedro Ludovico Teixeira, 2º andar
    Setor Central, Goiânia/GO – CEP: 74.015-908
    Atendimento: 08h às 12h e 14h às 18h

    Caso o usuário deseje saber a localização do Gabinete da Secretaria de Estado da Retomada, responda essas informações:
    Praça Dr. Pedro Ludovico Teixeira (praça cívica), Rua 82, N.º03, Setor Central
    Goiânia–GO- CEP 73003-010
    Telefone: (62) 3030-1590
    E-mail: gabinete.retomada@goias.gov.br
    Atendimento Presencial de segunda a sexta das 08h às 12h e das 14h às 18h

    Caso o usuário deseje saber a localização do Centro de Referência do Artesanato de Goiás (Gabinete da Secretaria), responda essas informações:
    Praça Dr. Pedro Ludovico Teixeira (Praça Cívica), nº 26
    Setor Central, Goiânia/GO – CEP: 74.015-908
    Atendimento: 08h às 12h e 14h às 18h

    Caso o usuário deseje saber a localização da Central Mais Empregos, responda essas informações:
    Avenida Araguaia, esquina com a Rua 15,
    Setor Central, Goiânia/GO – CEP: 74.110-130
    WhatsApp: (62) 98231-0070
    Atendimento: 08h às 18h
    
    Caso o usuário deseje saber a localização do Centro de Convenções Oscar Niemeyer – CCON, responda essas informações:
    Avenida Araguaia, esquina com a Rua 15,
    Av. Dep. Jamel Cecílio, Km 01
    Chácaras Alto da Glória, Goiânia/GO – CEP: 74891-135
    Telefone: (62) 3030-1488
    Atendimento: 08h às 12h e 14h às 17h
    
    Caso o usuário deseje saber a localização do Centro de convenções de Anápolis – CCA, responda essas informações:
    Avenida Araguaia, esquina com a Rua 15, nº 208
    Rodovia Transbrasiliana, Viviam Parque 2ª Etapa
    Anápolis-GO – CEP: 75001-970
    Telefone: (62) 3771-0898
    Atendimento: 08h às 12h e 14h às 17h
    ''',
)