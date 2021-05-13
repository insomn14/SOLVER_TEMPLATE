import gmpy2
from Crypto.Util.number import long_to_bytes as ltb

def main():
	n = int(input("Insert Modulus n : "))
	e = int(input("Insert Exponent e : "))
	c = int(input("Insert Ciphertext c : "))

	gs = gmpy2.mpz(c)
	gm = gmpy2.mpz(n)
	g3 = gmpy2.mpz(e)

	root, _ = gs.root(g3)
	print(ltb(root))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(e)