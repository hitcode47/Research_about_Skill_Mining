def gerar_dados_pessoais(data): 
    """
    Recolhimento das informações de usuário.
    """    
    Dados = {
        "Nome" : data['name'],
        "Numero de Repositorios" : data['public_repos'],
        "Endereço" : data['location'],
        "Bio" : data['bio'],   
    }
    return Dados
        
    
