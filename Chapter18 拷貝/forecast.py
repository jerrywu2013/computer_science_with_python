# L-18 MCS 260 : forecast.py
"""
Sample program to retrieve five day weather forecast from
http://weather.noaa.gov/pub/data/forecasts/state/il/ilz013.txt
"""
from urllib.request import urlopen
HOST = 'http://weather.noaa.gov/'
FCST = '/pub/data/forecasts/state/'
URL = HOST + FCST + '/il/ilz013.txt'
print('opening ' + URL + ' ...\n')
DATA = urlopen(URL)
while True:
    LINE = DATA.readline().decode()
    if LINE == '':
        break
    L = LINE.split(' ')
    if 'FCST' in L:
        LINE = DATA.readline().decode()
        print(LINE + DATA.readline().decode())
    if 'CHICAGO' in L:
        LINE = LINE + DATA.readline().decode()
        LINE = LINE + DATA.readline().decode()
        print(LINE + DATA.readline().decode())
