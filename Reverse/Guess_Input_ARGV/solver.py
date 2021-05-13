#!/usr/bin/python3
import subprocess
from string import printable


comp = ['114', '20', '119', '59', '104', '47', '75', '56', '81', '99', '23', '71', '56', '75', '124', '31', '65', '32', '77', '55', '103', '31', '96', '18', '76', '41', '27', '122', '29', '47', '83', '33', '78', '59', '10', '56', '15', '34', '94']

flag = 'rgbCTF{'
while len(flag) != len(comp):
	for ch in printable:
		argv = flag + ch
		args = map(str, ('./itJX.so', argv))

		popen = subprocess.Popen(args, stdout=subprocess.PIPE)
		popen.wait()
		output = popen.stdout.read().decode('ascii')[1:-2].split(', ')
		if all(i==j for i,j in zip(output, comp)):
			flag += ch
			print(f'Found : {flag}')
			break
print(flag)