def gerar_dados_pessoais(data): 
    Dados = {
            "Nome" : data['name'],
            "Numero de Repositorios" : data['public_repos'],
            "Endereço" : data['location'],     
    }
    return Dados
        
    
