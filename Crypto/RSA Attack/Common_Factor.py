def gcd(num1,num2):
	if num1 < num2:
		num1, num2 = num2, num1
	while num2 != 0:
		num1, num2 = num2, num1 % num2
	return num1

def is_common_factor(n1, n2):
	if gcd(n1, n2) == 1:
		return False
	else:
		return True

def get_pq(n1, n2):
	if is_common_factor(n1,n2):
		p = gcd(n1, n2)
		q = n1 / p

		return n1, p, q

def main():
	N1 = int(input("Insert Modulus N1 : "))
	N2 = int(input("Insert Modulus N2 : "))

	N, P, Q = get_pq(N1,N2)
	print("N : %d\np : %d\nq : %d"%(N,P,Q))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(e)