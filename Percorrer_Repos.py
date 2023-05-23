import requests
header = {
'Authorization' : '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',
"Accept": "application/vnd.github.v3+json"
}
def soma_de_linguagens(data):
    
    buscar_repositorios()
    varrer_repositorios(buscar_repositorios())
    listar_linguagens(varrer_repositorios())
    
def buscar_repositorios(data, header):
    repositorios = requests.get(data['repos_url'], headers=header)
    if repositorios.status_code == 200:
        repositorios = repositorios.json()
    else:
        print("Erro na camada de de repositorios")
        print("Erro: %d" %repositorios.status_code)
    return repositorios

def varrer_repositorios(repositorios):
    for repo in repositorios: 
        dados_link = requests.get(repo['languages_url'], headers=header)
        
        if dados_link.status_code == 200:
            dados = dados_link.json()
        else:
            print("Erro na camada de dados.link")
            print("Erro: %d" %dados_link.status_code)
            break
    return dados    
     
def listar_linguagens(dados):
    soma_linguagens = {}
    for language, valor in dados.items():
        if language in soma_linguagens:
            soma_linguagens[language] += valor
        else:
            soma_linguagens[language] = valor
    return soma_linguagens
