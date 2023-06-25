"""
Este módulo realiza o recolhimento de informações básicas do usuário para
formar o cabeçalho do arquivo.
"""
def gerar_dados_pessoais(data):
    """
    Gera dados pessoais a partir dos dados fornecidos.

    Parâmetros:
    dict: um dicionário contendo informações sobre o usuário.

    Retorna:
    dict: Um dicionário contendo os dados pessoais gerados.
    """
    dados = {
        "Nome" : data['name'],
        "Numero de Repositorios" : data['public_repos'],
        "Endereço" : data['location'],
        "Bio" : data['bio'],
    }
    return dados
        