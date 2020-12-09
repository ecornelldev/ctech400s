import requests
import time

URL = 'http://api.open-notify.org/iss-now.json'
j1 = requests.get(URL).json()
time.sleep(10)
j2 = requests.get(URL).json()

time_diff = abs(int(j2['timestamp']) - int(j1['timestamp']))
lat_diff = abs(float(j2['iss_position']['latitude']) - float(j1['iss_position']['latitude']))
long_diff = abs(float(j2['iss_position']['longitude']) - float(j1['iss_position']['longitude']))

print('The ISS has traveled ' + str(lat_diff) + ' degrees of latitude and ' + str(long_diff) + ' degrees of longitude in ' + str(time_diff) + ' seconds.')
