import gmpy2
from Crypto.Util.number import long_to_bytes as ltb

def gcd(num1,num2):
	if num1 < num2:
		num1, num2 = num2, num1
	while num2 != 0:
		num1, num2 = num2, num1 % num2
	return num1

def main():
	N  = int(input("Insert Modulus\t: "))
	c1 = int(input("Ciphertext1\t: "))
	c2 = int(input("Ciphertext2\t: "))
	e1 = int(input("Pub exponent1\t: "))
	e2 = int(input("Pub exponent2\t: "))

	a = gmpy2.invert(e1,e2)
	b = (float(gcd(e1, e2)-(a*e1)))/float(e2)

	i = gmpy2.invert(c2, N)
	mx = pow(c1, a, N)
	my = pow(i, int(-b), N)
	m = mx * my % N
	
	print(ltb(m))
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(e)
