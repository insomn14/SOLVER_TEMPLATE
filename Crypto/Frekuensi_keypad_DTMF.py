def map(data):
	mapping = {
		'1209-697': '1',
		'1209-770': '4',
		'1209-852': '7',
		'1209-941': '*',
		'1336-697': '2',
		'1336-770': '5',
		'1336-852': '8',
		'1336-941': '0',
		'1477-697': '3',
		'1477-770': '6',
		'1477-852': '9',
		'1477-941': '#',
		'1633-697': 'A',
		'1633-770': 'B',
		'1633-852': 'C',
		'1633-941': 'D'
	}
	result = ''
	for fq in data:
		result += mapping[fq]
	return result

def main():
	data = str(input('Input Frequency : ')).split(' ')
	print(data)

if __name__ == '__main__':
	main()