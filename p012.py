from p047 import primeFactors
from p010 import getPrimes

def divisors(N,primos):
	facts = primeFactors(N,primos)
	divs = 1
	factset = set()
	for f in facts:
		factset.add( (f,facts.count(f)) )
	for (p,e) in factset:
		divs *= e+1
	return divs 

def triangle(N):
	tri = 0
	for i in range(1,N+1):
		tri += i
	return tri

if __name__ == '__main__':	
	found = False
	i = 0
	tri = triangle(i)
	primos = getPrimes(20000000)
	while not found:
		divs = divisors(tri,primos)
		print("O triangulo #{0} - {1} tem {2} divisores".format(i,tri,divs))
		if divs >= 500:
			found = True
			print("Terminado")
		else:
			i += 1
			tri += i