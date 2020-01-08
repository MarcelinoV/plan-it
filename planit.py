# planit.py - returns weather and map of city
# Modules used
import requests, webbrowser, jsons, os
import pyinputplus as pyip

# API key, API call link, user input
# of city, all linked in a single object
# to create whole url address

# os mod is used to leave API key out of code
api_key = os.environ.get("opweather_api_key")
api_call = 'http://api.openweathermap.org/data/2.5/weather?q='
city_name = input('Enter City Name: ')
whole_url = api_call + city_name + "&appid=" + api_key

# get method of requests mod stored
response = requests.get(whole_url)

# data available in json form,
# so we convert json to python using json method
x = response.json()

# printed x earlier to see that x
# is a list of nested dictionaries
# print(x)

# if value of "cod" is 404, there'd be an error
# which means the city doesn't exist
# thus the code below:
if x['cod'] != '404':

    # value of "main" key stored in y
    y = x['main']

    # value of "temp" key from y
    # converted to fahrenheit, originally in kelvin
    current_temperature = (y['temp'] - 273.15) * (9 / 5) + 32

    # value of "pressure" key from y
    current_pressure = y['pressure']

    # value of "humidity" key from y
    current_humidity = y['humidity']

    # value of "weather" key stored in z
    z = x['weather']

    # value of "description" key at 0th index of z
    weather_description = z[0]['description']

    # print following values
    print(
        'Temperature in Fahrenheit: ' +
        str(current_temperature) +
        '\n Pressure in hPa unit: ' +
        str(current_pressure) +
        '\n Humidity in percentage: ' +
        str(current_humidity) + '%' +
        '\n Description: ' +
        str(weather_description)
    )

else:
    print('City not found.')

# optional option to open map of city
# utilizes pyinputplus mod for automatic input error catching
google_map = pyip.inputYesNo('Open Google Map of {}?'.format(city_name))

if google_map == 'yes':
    # utilizes webbrowser mod to open Google map
    webbrowser.open('https://www.google.com/maps/place/' + city_name)
    print('Opening map of {}'.format(city_name))

else:
    print('Thanks for using this program.')

# I hope to come back to this and add the option to find nearby hotels and restaurants
# credits to geeksforgeeks & automate the boring stuff with python for inspiration
