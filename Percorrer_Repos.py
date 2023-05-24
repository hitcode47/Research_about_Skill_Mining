import requests
header = {
'Authorization' : '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',
"Accept": "application/vnd.github.v3+json"
}

def soma_de_linguagens(data):
    
    _repositorio = buscar_repositorios(data)
    _dados = varrer_repositorios(_repositorio)
    _soma_final = listar_linguagens(_dados)
    return _soma_final

def buscar_repositorios(Par_data):
    repositorios = {}
    response = requests.get(Par_data['repos_url'], headers=header)
    if response.status_code == 200:
        repositorios = response.json()
    else:
        print("Erro na camada de de repositorios")
        print("Erro: %d" %response.status_code)
        
    return repositorios

def varrer_repositorios(Par_repositorio):
    dados = {}
    for repo in Par_repositorio: 
        dados_link = requests.get(repo['languages_url'], headers=header)
        
        if dados_link.status_code == 200:
            dados = dados_link.json()
        else:
            print("Erro na camada de dados.link")
            print("Erro: %d" %dados_link.status_code)
            break
    return dados    
     
def listar_linguagens(Par_dados):
    soma_linguagens = {}
    somatorio = sum(Par_dados.values())
    
    for language, valor in Par_dados.items():
        if language in soma_linguagens:
            soma_linguagens[language] += valor
        else:
            soma_linguagens[language] = valor
            
    for language, valor in soma_linguagens.items():
        percentual = (valor/somatorio)*100
        percentual = round(percentual, 2)
        soma_linguagens[language] = [valor, f"valor percentual = {percentual}%"]
    return soma_linguagens