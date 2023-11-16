import time
import requests
from datetime import datetime as dt
import smtplib

MY_LAT = 18.520430
MY_LONG = 73.856743


def is_satellite_overhead():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'long': MY_LONG,
        'formatted': 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()['results']

    sunrise = int(data['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['sunset'].split('T')[1].split(':')[0])

    tnow = dt.now().hour

    if tnow >= sunset or tnow <= sunrise:
        return True

my_email = "sample@gmail.com"
password = 'ansbcjhdsvcjvhdsc'

while True:
    time.sleep(60)
    if is_night() and is_satellite_overhead():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg='Subject:Lookup\n\n The satellite is above you in the sky')
        break
