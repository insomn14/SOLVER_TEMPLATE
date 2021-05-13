import re
import json
import requests, urllib3.request
from bs4 import BeautifulSoup
from string import ascii_uppercase as upper

# https://gps-coordinates.org/coordinate-converter.php
def getplace(loc):
    query = urllib3.request.urlencode({
        'loc' : loc,
        'lang' : 'en-GB'
    })

    jwt = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJtYXBzYXBpIiwidGlkIjoiWUg2V005S1o0VSIsImFwcGlkIjoiWUg2V005S1o0VS5tYXBzLm9yZy5ncHMtY29vcmRpbmF0ZXMiLCJpdGkiOmZhbHNlLCJpcnQiOmZhbHNlLCJpYXQiOjE2MDQ5MjY0NzQsImV4cCI6MTYwNDkyODI3NH0.Z27I-zId05Wgt9OfDKB65LYMvSOAEiooCA7r5etcpekdCc4HRYxG46R-jqlQc7t4dUsx4GgfTl5B0ztZdi0NPA'
    headers = {'Authorization': jwt}
    link = 'https://api.apple-mapkit.com/v1/reverseGeocode?'
    while True:
        try:
            req = requests.get(link+query, headers=headers)
            if req.status_code == 200:
                resp = json.loads(req.text)
                country = resp['results'][0]
                if 'country' in country.keys():
                    return country['country']
                else:
                    return conutry['name']
        except KeyboardInterrupt:
            exit()
        except Exception:
            continue

def main():
    fileloc = open('enc.txt', 'r').read().strip()
    data = re.findall(r'[0-9-., ]+', fileloc)

    flag = 'IHOPEYOUENJOYEDGOINGONTHATREALLYLONGGLOBALTOUR'
    for cnt in range(len(flag), len(data)):
        print(f'[!] Latitude, Longitude : {data[cnt]}')
        country = getplace(data[cnt])
        flag += country[0]
        print(f'[*] Found : {country}')
        print(f'[+] FLAG ({cnt+1}/{len(data)}) : {flag}')
        print('-'*20)

if __name__ == '__main__':
    main()
