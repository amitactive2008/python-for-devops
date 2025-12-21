import requests
import json
import os

API_KEY=os.environ['API_KEY'] 
region='New Delhi'
wether_url=f'https://api.weatherstack.com/current?&access_key={API_KEY}&query={region}'
file_name = 'output_file.json'

def get_wether():
    headers = {
        "Accept": "application/json"
    }

    wether_data=requests.get(url=wether_url,headers=headers).json()
    f = open('file_name', 'w', encoding='utf-8')
    json.dump(wether_data,f)
    f.close()
   
    sunrise=wether_data['current']['astro']['sunrise']
    sunset=wether_data['current']['astro']['sunset']
    print(f'Sunrise Time is : {sunrise}')
    print(f'Sun set Time is : {sunset}')

get_wether()