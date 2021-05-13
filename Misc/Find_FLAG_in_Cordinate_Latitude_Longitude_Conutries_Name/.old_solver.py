import re
import json
import urllib, urllib.request
from string import ascii_uppercase as upper
from bs4 import BeautifulSoup


def getplace(lat, lon):
    query = urllib.parse.urlencode({
        'lat' : lat,
        'latlon_digits' : 'true',
        'lon' : lon,
        'zoom' : 5,
        'minlon' : 0,#15.238037109375002,
        'minlat' : 0,#46.41513877649202,
        'maxlon' : 0,#26.400146484375004,
        'maxlat' : 0#48.09275716032736
    })
    source = ['https://www.openstreetmap.org/geocoder/search_geonames_reverse?', 'https://www.openstreetmap.org/geocoder/search_osm_nominatim_reverse?']
    while True:
        try:
            for link in source[::-1]:
                req = urllib.request.urlopen(link+query)
                if req.getcode() == 200:
                    soup = BeautifulSoup(req.read().decode('utf-8'), 'html5lib')
                    country = soup.text.strip().split(', ')
                    if 'No results found' not in country:
                        print(f'[*] Country : {country}')
                        return country[-1]
        except Exception:
            continue

def main():
    fileloc = open('enc.txt', 'r').read().strip()
    data = re.findall(r'[0-9-., ]+', fileloc)

    flag = ''
    for loc in data:
        try:
            lat, lon = loc.split(', ')
            country = getplace(lat, lon)
            flag += ''.join(c for c in country if c in upper)[0]
            print(f'[+] Found {loc} : {country}')
            print(f'[+] FLAG : {flag}')
        except IndexError:
            flag += '_'
            print(f'[+] Found {loc} : {country}')
            print(f'[+] FLAG : {flag}')

if __name__ == '__main__':
    main()
