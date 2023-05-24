import json
import requests
header = {
    'Authorization': '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',
    "Accept": "application/vnd.github.v3+json"
}
def commit_Por_Nome(Data):
    
    _repositorio = requisitar_repositorio(Data)
    varrer_repositorio_de_commits(_repositorio)

    
def requisitar_repositorio(Data):
    response = requests.get(Data['repos_url'], headers=header)
    if response.status_code == 200:
        repositorios = response.json()
    else:
        print("Erro na camada de repositorio - Gerenciador de commits ")
        print("Erro: %d" %response.status_code)
    return repositorios

def varrer_repositorio_de_commits(repositorios):
    
    for repo in repositorios:
        repo_response = requests.get(repo['commits_url'], headers=header)
        if repo_response.status_code == 200:
            repos_commits = repo_response.json()
        else:
            print ("Erro na camade de repositorio de commits")
            print("Erro: %d" %repo_response.status_code)
            break
    Commit_Por_Repositorio = {
        
    }
    for repo_commit in repos_commits:
        if repo_commit['commit'] != None:
            Commit_Por_Repositorio[repo['name']] += 1
        else:
            print ("Erro de soma de commits")
    return Commit_Por_Repositorio




    