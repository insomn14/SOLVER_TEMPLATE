import gmpy2

def main():
	N1 = int(input("Insert Modulus N1\t: "))
	N2 = int(input("Insert Modulus N2\t: "))
	N3 = int(input("Insert Modulus N3\t: "))
	c1 = int(input("Ciphertext1\t: "))
	c2 = int(input("Ciphertext2\t: "))
	c3 = int(input("Ciphertext3\t: "))
	e = int(input("Exponent\t: ")) # e = 3 example

	tA = c1 * (N2*N3) * gmpy2.invert(N2*N3, N1)
	tB = c2 * (N1*N3) * gmpy2.invert(N1*N3, N2)
	tC = c3 * (N1*N2) * gmpy2.invert(N1*N2, N3)

	c = (tA + tB + tC) % (N1*N2*N3)

	m = gmpy2.root(c,e)[0]
	print(m)
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(e)