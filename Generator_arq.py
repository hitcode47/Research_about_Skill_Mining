def gerar_dados_pessoais(data): 
    """
    Recolhimento das informações de usuário.
    """    
    dados = {
        "Nome" : data['name'],
        "Numero de Repositorios" : data['public_repos'],
        "Endereço" : data['location'],
        "Bio" : data['bio'],   
    }
    return dados
        
    
