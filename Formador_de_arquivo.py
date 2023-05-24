import json
import Generator_arq
import Percorrer_Repos
import Gerenciador_Commits

def gerar_arquivo_de_dados(data):
    Dados = {
        "Dados Pessoais" : Generator_arq.gerar_dados_pessoais(data),
       "Atividade de cada linguagem em bytes" : Percorrer_Repos.soma_de_linguagens(data),
        #"Numero de Commits Por linguagem" : Gerenciador_Commits.commit_Por_Nome(data)
    }
    with open('Arquivo de dados.txt', 'w') as Arquivo:
        json.dump(Dados, Arquivo, indent=4)

    
