import requests

API_ENDPOINT = 'https://api.pokemontcg.io/v1'

def perform_request(endpoint, params={}):
    url = '{}/{}'.format(API_ENDPOINT, endpoint)
    return requests.get(url, params=params).json()