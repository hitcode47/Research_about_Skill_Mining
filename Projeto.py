import requests
from formador_de_arquivo import gerar_arquivo_de_dados
"""
Requisição da primeira camadade de dados da API rest do Github.
"""
URL = 'https://api.github.com/users/hitcode47'
header = {
    'Authorization': 'github_pat_11A7FEEZY02yM3K6OLmzlk_eXWaBbAVfr4q2nkC6'
                     'bkIDAbmcBe1ETIqizTNTEOLPchORHRBXQYON8EHtFH',
    'Accept': 'application/vnd.github.v3+json',
}
response = requests.get(URL, headers=header, timeout = 5)
if response.status_code == 200:
    data_user = response.json()
    gerar_arquivo_de_dados(data_user)
else:
    print("Erro de requisição")
    print(f"Erro: {response.status_code}")
