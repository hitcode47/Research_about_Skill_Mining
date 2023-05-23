import requests
from Formador_de_arquivo import gerar_arquivo_de_dados
    
url = "https://api.github.com/users/jesimonbarreto"
header = {
    'Authorization': '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',
    "Accept": "application/vnd.github.v3+json"
}

Data_user = requests.get(url, headers=header)

if Data_user.status_code == 200:
    Data_user = Data_user.json()
    gerar_arquivo_de_dados(Data_user)
    
else:
    print("Erro de requisição")
    print("Erro: %d" %Data_user.status_code)