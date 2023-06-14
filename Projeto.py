import requests
from Formador_de_arquivo import gerar_arquivo_de_dados

"""
Requisição da primeira camadade de dados da API rest do Github.
"""

url = 'https://api.github.com/users/CViniciusSDias'
header = {
    'Authorization': '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',
    'Accept': 'application/vnd.github.v3+json',
}
response = requests.get(url, headers=header)
if response.status_code == 200:
   data_user = response.json()
   gerar_arquivo_de_dados(data_user)
    
else:
   print("Erro de requisição")
   print("Erro: %d" %response.status_code)