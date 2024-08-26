import requests

# URL do endpoint onde o Flask está rodando
url = "http://localhost:5000/upload"

# Caminho para o arquivo CSV no seu sistema
file_path = "transaction_fact_v6_2018.csv"

# Abrir o arquivo CSV e fazer o upload
with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

# Imprimir a resposta do servidor
print(response.json())
