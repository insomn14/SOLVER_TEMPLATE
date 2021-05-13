import hashlib
from time import sleep

#f = open('hash.txt', 'r').read().split()[0]
f =  str(input('[?] Hash : ')) #'YELLOW-turkmenistan-PEACH:eaa8e5b2e1392708ae2800110c66ac0d'
fruits = open('fruit.txt', 'r').read().split('\n')
colors = open('colors.txt', 'r').read().split('\n')
country = open('country.txt', 'r').read().split('\n')
try:
    for col in colors:
        for con in country:
            for frt in fruits:
                gabung = col+'-'+con+'-'+frt
                result = hashlib.md5(gabung.encode()).hexdigest()
                #print f,'->',gabung
                if result == f:
                    print('Found FLAG :',gabung)
                    exit()

except KeyboardInterrupt as err:
    print(err)
