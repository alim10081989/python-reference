import requests
import os
from twilio.rest import Client


OWM_Endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
api_key = os.environ.get('OWM_API_KEY')
account_sid = os.environ.get('TWILIO_ACC_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

weather_params = {
    'lat': 19.075983,
    'long': 72.877655,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+10123456789',
        body='Kindly take a umbrella since it will rain today ☔',
        to='+911234567890'
    )

    print(message.status)


