import requests

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

print(type(avaliacoes.json()))