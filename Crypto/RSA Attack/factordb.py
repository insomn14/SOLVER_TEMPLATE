import os, re, requests
from bs4 import BeautifulSoup as bs

def template(p, q, n, e, c):
    tmp = f'''#!/usr/bin/env python3
from Crypto.Util.number import inverse, long_to_bytes

p = {p}
q = {q}
e = {e}
n = {n}
c = {c}

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = long_to_bytes(pow(c, d, n))
print(m.decode('utf-8'))'''
    with open('solver.py', 'w') as out:
        out.write(tmp)
        out.close()
    print('[+] Successfuly create solver.py')

def main():
    status = {
            'C': 'Composite, no factors known',
            'CF': 'Composite, factors known',
            'FF': 'Composite, fully factored',
            'P': 'Definitely prime',
            'Prp': 'Probably prime',
            'U': 'Unknown',
            'Unit': 'Just for "1"',
            'N': 'This number is not in database (and was not added due to your settings)'
            }


    n = input('[?] n : ')
    e = input('[?] e : ')
    c = input('[?] c : ')

    url = f'http://factordb.com/index.php?query={n}'
    req = requests.get(url)
    if req.status_code == 200:
        fdb_status = re.findall(r'<td>(\w+)</td>', req.text)[0]
        if fdb_status == 'FF':
            print(f'[*] Status : {status[fdb_status]}')
            soup = bs(req.text, 'html5lib')
            p,q = [xx.text for xx in soup.findAll('font', {'color':"#000000"})]
            return template(p, q, n, e, c)
        else:
            print(f'[*] Status : {status[fdb_status]}')

if __name__ == '__main__':
    main()

