import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
headers = {
    'X-Gismeteo-Token': '1382b8cb-5428-42e7-9018-d4042e800c01'
}
url_base = 'https://api.gismeteo.net/v2/search/cities/?'


def get_weather(city_name: str):
    params = {
        'query': city_name,
    }
    response = requests.get(url=url_base, headers=headers, params=params)
    print(response.json())
