import requests
import json
from datetime import datetime

#---------------------------

time = datetime.now()
my_time = time.time()


#MY TIME AND LOC INFO ABOVE ->

#---------------------------

sun_api_url = 'https://api.sunrisesunset.io/json?lat=19.0414&lng=-98.2063&timezone=America/Chicago'

sun_data = requests.get(url=sun_api_url)

sun_data_json =sun_data.json()

sunset = sun_data_json['results']['sunset']
sunrise = sun_data_json['results']['sunrise']

print(sunset)
print(sunrise)
print(f'my time : {my_time}')
#api sun above


'''
api_url = 'http://api.open-notify.org/iss-now.json'

data = requests.get(url=api_url)

print('\n')

json_data = data.json()

list_keys = list(json_data.keys())
print(list_keys)

for key in list_keys:
    print(json_data[key])
    print('\n')


'''

#LEARN GIT STOP F***** COPYING AND PASTING UR OWN CODE
