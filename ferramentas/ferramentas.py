import requests
from bs4 import BeautifulSoup


def extrair_texto_pagina_web(url: str, inicio_apos: str = "Transparência Fale Conosco", fim_antes: str = "Governo na") -> dict:
    """
    Extrai e armazena o texto de uma página web

    Args:
        url (str): URL da página web

    Returns:
        str: Texto extraído da página web
    """
    try:
        # Fazer requisição HTTP
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Parse do HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Remover scripts, estilos e outros elementos não desejados
        for script in soup(["script", "style", "meta", "link"]):
            script.decompose()

        # Extrair texto
        texto = soup.get_text()

        # Limpar o texto (remover espaços extras e quebras de linha múltiplas)
        linhas = (linha.strip() for linha in texto.splitlines())
        chunks = (frase.strip() for linha in linhas for frase in linha.split("  "))
        texto_limpo = ' '.join(chunk for chunk in chunks if chunk)

        texto_final = texto_limpo

        # Delimitar início
        if inicio_apos:
            pos_inicio = texto_limpo.find(inicio_apos)
            if pos_inicio != -1:
                texto_final = texto_limpo[pos_inicio + len(inicio_apos):]
            else:
                print(f"Palavra de início '{inicio_apos}' não encontrada")

        # Delimitar fim
        if fim_antes:
            pos_fim = texto_final.find(fim_antes)
            if pos_fim != -1:
                texto_final = texto_final[:pos_fim]
            else:
                print(f"Palavra de fim '{fim_antes}' não encontrada")

        return {"texto_extraido": texto_final}

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None


# Exemplo de uso
url = "https://goias.gov.br/retomada/perguntas-frequentes-sobre-o-programa-mais-empregos/"
texto = extrair_texto_pagina_web(url)
if texto:
    print("Texto extraído com sucesso!")
    print(texto["texto_extraido"])