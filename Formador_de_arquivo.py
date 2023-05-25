import json
import Generator_arq
import Percorrer_Repos
import Gerenciador_Commits

def gerar_arquivo_de_dados(data):
    """
    Estruturação de dados colhidos em formato de dicionários e armazenamento em arquivos.
    """
    Dados = {
       "Dados Pessoais" : Generator_arq.gerar_dados_pessoais(data),
       "Atividade de cada linguagem em bytes" : Percorrer_Repos.soma_de_linguagens(data),
        #"Numero de Commits Por linguagem" : Gerenciador_Commits.commit_Por_Nome(data)
    }
    Nome_do_arquivo = input('inserir nome do arquivo que irá armazenar os dados do usuário: ')
    with open(Nome_do_arquivo +'.txt', 'w', encoding='utf-8') as Arquivo:
         json.dump(Dados, Arquivo, indent=4, ensure_ascii=False)