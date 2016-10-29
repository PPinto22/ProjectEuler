# Goldbach's other conjecture

from p010 import getPrimes
from p010 import isPrime

if __name__ == '__main__':
	n = 9
	conjecture = True
	primos = getPrimes(10000)
	while conjecture:
		i = 0
		for i in range(0,len(primos)):
			encontrado_i = False
			for j in range(1,10000):
				val = primos[i] + 2*j**2
				if val == n:
					#print("n = {0}, p = {1}, j = {2}".format(n,primos[i],j))
					encontrado_i = True
					break
				elif val > n:
					break
			if encontrado_i:
				break
		if not encontrado_i:
			conjecture = False
		else:
			n += 2
			while isPrime(n):
				n += 2
	print(n)



