import time
import requests
header = {
'Authorization' :'github_pat_11A7FEEZY02yM3K6OLmzlk_eXWaBbAVfr4q'
                 '2nkC6bkIDAbmcBe1ETIqizTNTEOLPchORHRBXQYON8EHtFH',                 
'Accept':'application/vnd.github.v3+json'
}
def soma_de_linguagens(data):
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
    """
    -Recebe a camada inicial ofertada pela API Rest do Github.
    -Entra na camada de repositório.
    -Retorna a camada com repositórios. 
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
    """
    -Recebe o dados da função Buscar_repositorio()
    -Acessa a camada de Bytes por linguagem
    -Cria dicionario com cada linguagem e a quantidade de dados enviados
    -Retorna dicionario de Bytes/linguagens
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
