"""Módulo que soma o número de bytes por linguagem.

Returns:
    dict: dicionario com o nome de cada linguagem e sua respectiva quantidade em bytes.
"""
import time
import requests
header = {
'Authorization':
    'github_pat_11A7FEEZY02yM3K6OLmzlk_eXWaBbAVfr4q'
    '2nkC6bkIDAbmcBe1ETIqizTNTEOLPchORHRBXQYON8EHtFH',                 
'Accept':
    'application/vnd.github.v3+json'
}
def soma_de_linguagens(data):
    """Executa as funções do módulo

    Args:
        data (dict): endpoint base da API rest do github

    Returns:
        dict: retorna o valor retornado pela função 'listar_linguagens()'.
    """
    try:
        repositorio = buscar_repositorios(data)
    except requests.exceptions.RequestException:
        time.sleep(7200)
        repositorio = buscar_repositorios(data)
    try:
        dado = varrer_repositorios(repositorio)
    except requests.exceptions.RequestException:
        time.sleep(7200)
        dado = varrer_repositorios(repositorio)
    return listar_linguagens(dado)

def buscar_repositorios(parametro_data):
    """Acessar a camada de repositório

    Args:
        data (dict): Endpoint base da API rest do github

    Returns:
        dict: Retorna todos os repositórios de um perfil
    """
    repositorios = {}
    response = requests.get(parametro_data['repos_url'], headers=header, timeout=5)
    if response.status_code == 200:
        repositorios = response.json()
    else:
        print("Erro na camada de de repositorios")
        print(f"Erro: {response.status_code}")
    return repositorios

def varrer_repositorios(parametro_repositorios):
    """Acessa a camada linguagens de cada repositório

    Args:
        data (dict): Dicionário com todos repositórios de um usuario

    Returns:
        dict: Dicionário com todos todas as linguagens e suas respectivas quantidades de bytes.
    """
    dados = {}
    dados_link = {}
    for repo in parametro_repositorios:
        dados_link = requests.get(repo['languages_url'], headers=header, timeout=5)
        if dados_link.status_code == 200:
            dados_repo = dados_link.json()
            dados.update(dados_repo)
        else:
            print("Erro na camada de dados.link")
            print(f"Erro: {dados_link.status_code}")
            break
    return dados
def listar_linguagens(parametro_de_dados):
    """Soma a quantidade de bytes em linguagens de mesmo nome.

    Args:
        parametro_de_dados (_type_): dicionário com linguagens(nomes repetidos)
        e sua respectiva quantidade de bytes.

    Returns:
        dict: numero de bytes por linguagens, valor percentual em relação ao todo
        e linguagem mais utilizada. 
    """
    soma_linguagens = {}
    somatorio = sum(parametro_de_dados.values())
    valor_maximo = max(parametro_de_dados)
    multiplicador_percentual = 100
    for language, valor in parametro_de_dados.items():
        if language in soma_linguagens:
            soma_linguagens[language] += valor
        else:
            soma_linguagens[language] = valor
    for language, valor in soma_linguagens.items():
        percentual = (valor/somatorio)*multiplicador_percentual
        percentual = round(percentual, 2)
        soma_linguagens[language] = [f"valor em bytes: {valor}",
                                     f"valor percentual em relação ao total: {percentual}%"]
    soma_linguagens["Linguagem mais utilizada"] = valor_maximo
    return soma_linguagens
