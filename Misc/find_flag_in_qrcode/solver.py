#!/usr/bin/env python3

import os, re
from PIL import Image
from pyzbar.pyzbar import decode

fname = os.listdir()


for fl in sorted(fname):
	ct =  int(''.join(re.findall('\d',fl)))
	# print(f'[+] Testing {ct} : ', end='')
	data = decode(Image.open(fl))
	if data[0].data != b'RESTCON{FAKEFLAG%d}' %(ct):
		print('Found : ',data[0].data)
		exit()