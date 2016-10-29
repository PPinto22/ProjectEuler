# Prime permutations

from p024 import permutations
from p010 import isPrime
from p010 import getPrimesSet

def getPrimePermutations(prime):
	ps = permutations(list(str(prime)))
	psInt = set()
	for p in ps:
		psInt.add(int(p))
	ps = list(filter(lambda x: isPrime(x), psInt))
	if len(ps) >= 3:
		for i in range(0,len(ps)-2):
			for j in range(i+1,len(ps)-1):
				for k in range(j+1,len(ps)):
					yield sorted( (ps[i],ps[j],ps[k]) )

if __name__ == '__main__':
	rs = set()
	primos = getPrimesSet(9999)
	for p in primos:
		if p > 1000:
			for (a,b,c) in getPrimePermutations(p):
				if b-a == c-b and a>1000:
					rs.add( (a,b,c) )
	for (a,b,c) in rs:
		print(str(a)+str(b)+str(c)) 