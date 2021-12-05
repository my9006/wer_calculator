import requests


def request_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Dark", params={'type': 'single'})
    response_joke = dict(response.json()).get('joke')
    return response_joke
