import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
headers = {
    'X-Gismeteo-Token': os.getenv('TOKEN_API')
}
url_base_search = 'https://api.gismeteo.net/v2/search/cities/?'
url_get_weather_id = 'https://api.gismeteo.net/v2/weather/current/'


def search_city_name(city_name: str):
    params = {
        'query': city_name,
    }
    response = requests.get(url=url_base_search, headers=headers, params=params)
    data_json = response.json()
    results_search = data_json.get('response').get('items')
    for item in results_search:
        if item.get('name') == city_name:
            return str(item.get('id'))
    print('City not found')


def get_weather(city_id: str):
    response = requests.get(url=url_get_weather_id + city_id, headers=headers)
    data_json = response.json().get('response')
    temperature_air = str(data_json.get('temperature')['air']['C']) + ' °C'
    temperature_water = str(data_json.get('temperature')['water']['C']) + ' °C'
    description = data_json.get('description')['full']
    return {'Погода': description,
            'Температура воздуха': temperature_air,
            'Температура воды': temperature_water,
            }


def get_forecast(city_name: str):
    city_id = search_city_name(city_name)
    return get_weather(city_id)
