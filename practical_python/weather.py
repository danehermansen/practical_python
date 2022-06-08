import requests
def get_weather_desc_temp():
    
    city = 'Orlando'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=city&appid=api_key'

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get('weather')[0].get('description')


weather_dict = get_weather_desc_temp()
print("todays forecast is ", description)
