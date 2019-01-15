from django.shortcuts import render
import json
import requests
#from django.http import HttResponse

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=404d7b80e842155d20b3d2c3f1a0604c'
    
    city = 'Kiev'
       
    weather_data = []

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    weather_data.append(city_weather)

    context = {'weather_data' : weather_data}
    return render(request, 'micro_app/index.html', context)

        