from django.shortcuts import render, redirect

import json
import requests

with open('config.json') as config:
    config = json.load(config)

def index(request):
    if 'city' not in request.session:
        request.session['city'] = 'Chicago'

    base_url = 'http://api.openweathermap.org/data/2.5/weather/?'
    city = request.session['city']
    api_key = config['API_KEY']
    units = 'imperial'

    payload = {
        'q': city,
        'appid': api_key,
        'units': units
        }

    r = requests.get(base_url, params=payload).json()

    desc = r['weather'][0]['main']

    weather = {
        'city': city,
        'temp': r['main']['temp'],
        'desc': desc,
        'feels_like': r['main']['feels_like'],
        'low': r['main']['temp_min'],
        'high': r['main']['temp_max']
    }
    
    context = {
        'weather': weather
    }

    return render(request, 'index.html', context)

def query(request):
    request.session['city'] = request.POST['city']
    return redirect('/')

def flush(request):
    request.session.flush()
    return redirect('/')