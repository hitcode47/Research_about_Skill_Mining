"""
Este módulo contém funções para recolher e armazenar dados em arquivos.
"""
import json
import generator_arq
import percorrer_repositorio
import gerenciador_commits
def gerar_arquivo_de_dados(data):
    """
    Estruturação de dados colhidos em formato de dicionários e armazenamento em arquivos distintos.
    """
    dados = {
      # "Dados Pessoais" : generator_arq.gerar_dados_pessoais(data),
      # "Atividade de cada linguagem em bytes" : percorrer_repositorio.soma_de_linguagens(data),
       "Numero de Commits Por linguagem" : gerenciador_commits.commit_por_nome(data)
    }
    nome_do_arquivo = input('inserir nome do arquivo que irá armazenar os dados do usuário: ')
    with open(nome_do_arquivo +'.txt', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        