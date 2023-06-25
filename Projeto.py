"""
Requisição da primeira camadade de dados da API rest do Github.
"""
import requests
from formador_de_arquivo import gerar_arquivo_de_dados

URL = 'https://api.github.com/users/hitcode47'
header = {
    'Authorization': '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',
    'Accept': 'application/vnd.github.v3+json'
}
"""Os dados requisitados são passados como parâmetro na funçã: gerar_arquivo_de_dados().
"""
response = requests.get(URL, headers=header, timeout = 5)
if response.status_code == 200:
    data_user = response.json()
    gerar_arquivo_de_dados(data_user)
else:
    print("Erro de requisição")
    print(f"Erro: {response.status_code}")
