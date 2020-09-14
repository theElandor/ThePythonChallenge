#! python 3
##print the weather from command line

import json, requests, sys
import time
APPID = ''
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
print("Accessing online sources...")
time.sleep(2)
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % location
print("Access granted")
time.sleep(2)
print("saving data...")
time.sleep(2)
response = requests.get(url)
response.raise_for_status()
print("Printing raw data...")
time.sleep(2)
print(response.text)
weatherData = json.loads(response.text)  ##load json data in a python variable
print("data saved , printing weather...")
time.sleep(2)
w = weatherData['list']
print('Current weather in %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

