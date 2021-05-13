from sympy.solvers import solve
from sympy import Symbol

def cf_expansion(n, d):
	e = []

	q = n // d
	r = n % d
	e.append(q)

	while r != 0:
		n, d = d, r
		q = n // d
		r = n % d
		e.append(q)

	return e

def get_convergents(e):
	n = []
	d = []

	for i in range(len(e)):
		if i == 0:
			ni = e[i]
			di = 1
		elif i == 1:
			ni = e[i]*e[i-1] + 1
			di = e[i]
		else: # i > 1
			ni = e[i]*n[i-1] + n[i-2]
			di = e[i]*d[i-1] + d[i-2]

		n.append(ni)
		d.append(di)
		yield (ni, di)


def main():
	#e = 17993 #Public_exp here
	#N = 90581 #Modulus here
	e = int(input("Public_exp : "))
	N = int(input("Modulus : "))

	cf = cf_expansion(N, e)
	conv = get_convergents(cf)

	for pd, pk in conv:
		if pk == 0:
			continue

		possible_phi = (e*pd - 1)//pk
			
		x = Symbol('x', integer=True)
		roots = solve(x**2 + (possible_phi - N - 1)*x + N, x)

		if len(roots) == 2:
			p, q = roots

			if p * q == N:
				print ('p : ', p)
				print ('q : ', q)
				print ('d : ', pd)
				break

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(e)
