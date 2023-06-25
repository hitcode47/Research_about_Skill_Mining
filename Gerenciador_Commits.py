"""
Módulo que conta o número de commites por linguagem

Returns:
        dict: Quantidade de commites por linguagem
"""
import time
import requests
header = {
   'Authorization':'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',
   'Accept':'application/vnd.github.v3+json'
}
def commit_por_nome(data):
    """_summary_

    Args:
        data (dict): endpoint base da API rest do github

    Returns:
        dict: retorna quantidade de commites por linguagem
    """
    try:
        _repositorio = requisitar_repositorio(data)
    except requests.exceptions.RequestException:
        time.sleep(7200)
        _repositorio = requisitar_repositorio(data)
    try:
        return varrer_repositorio_de_commits(_repositorio)
    except requests.exceptions.RequestException:
        time.sleep(7200)
        return varrer_repositorio_de_commits(_repositorio)

def requisitar_repositorio(data):
    """_summary_

    Args:
        data (dict): Endpoint base da API rest do github

    Returns:
        dict: Acessa os repositórios de um perfil no github
    """
    response = requests.get(data['repos_url'], headers=header, timeout=5)
    if response.status_code == 200:
        repositorios = response.json()
    else:
        print("Erro na camada de repositorio - Gerenciador de commits ")
        print(f"Erro: {response.status_code}")
    return repositorios

def varrer_repositorio_de_commits(repositorios):
    """_summary_

    Args:
        repositorios (dict): Endpoint de repositorios da API rest do github

    Returns:
        dict: Valor da soma de repositório por linguagem
    """
    commit_por_repositorio = {}
    for repo in repositorios:
        repo_response = requests.get(f"https://api.github.com/repos/{repo['full_name']}/commits", headers=header, timeout=5)
        if repo_response.status_code == 200:
            repos_commits = repo_response.json()
        else:
            print ("Erro na camada de repositorio de commits")
            print(f"Erro: {repo_response.status_code}")
            break
        for name in repos_commits:
            autor = name['commit']['author']['name']
            if autor in commit_por_repositorio:
                commit_por_repositorio[autor] += 1
            else:
                commit_por_repositorio[autor] = 1
        return commit_por_repositorio
