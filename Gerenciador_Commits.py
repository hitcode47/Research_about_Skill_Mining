import requests
import time
header = {
    'Authorization': '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',
    'Accept': 'application/vnd.github.v3+json'
}
def commit_por_nome(data):
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
    response = requests.get(data['repos_url'], headers=header)
    if response.status_code == 200:
       repositorios = repositorios.json()
    else:
       print("Erro na camada de repositorio - Gerenciador de commits ")
       print("Erro: %d" %response.status_code)
    return repositorios

def varrer_repositorio_de_commits(repositorios):
    commit_por_repositorio = {}
    for repo in repositorios:
        repo_response = requests.get(repo['commits_url'], headers=header)
        if repo_response.status_code == 200:
           repos_commits = repos_commits.json()
        else:
           print ("Erro na camade de repositorio de commits")
           print("Erro: %d" %repo_response.status_code)
           break
        for repo_commit in repos_commits:
            if repo_commit['commit'] != None:
               commit_por_repositorio[repo['name']] += 1
            else:
               print ("Erro de soma de commits")
        return commit_por_repositorio




    