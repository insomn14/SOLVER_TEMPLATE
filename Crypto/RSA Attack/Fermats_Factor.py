import gmpy2

def fermat_factor(n):
	a = gmpy2.sqrt(n)
	b2 = a*a - n
	b = gmpy2.sqrt(n)
	while b2 != b*b:
		a += 1
		b2 += a*a - n
		b = gmpy2.sqrt(b2)

	factor1 = a + b
	factor2 = a - b

	assert n == factor1 * factor2
	return long(factor1.digits()), long(factor2.digits())

def main():
	p, q = fermat_factor(int(input("Masukan Nilai n : ")))
	print("p : %d\n q = %d\n"%(p,q))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(e)
