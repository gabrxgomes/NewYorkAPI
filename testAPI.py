import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API do New York Times
API_KEY = 'ZhGhzcnyXgrSF5lA7mvNqUXFd6v5PQCo'
BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

# Defina os parâmetros da consulta
params = {
    'q': 'technology',  # Termo de busca
    'api-key': API_KEY,
    'begin_date': '20230101',  # Data de início (YYYYMMDD)
    'end_date': '20231231'  # Data de término (YYYYMMDD)
}

try:
    # Faça a solicitação GET
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

    # Parseie a resposta JSON
    data = response.json()

    # Exiba os títulos das notícias e os URLs
    for i, article in enumerate(data['response']['docs']):
        print(f"{i + 1}. {article['headline']['main']}")
        print(f"URL: {article['web_url']}\n")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
