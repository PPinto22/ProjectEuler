# Distinct primes factors

from p010 import getPrimes

def primeFactors(n,primos=None):
	factors = list()
	if primos == None:
		primos = getPrimes(n)
	dividendo = n
	while dividendo > 1:
		for i in range(0,len(primos)):
			if dividendo % primos[i] == 0:
				factors.append(primos[i])
				dividendo = dividendo // primos[i]
				break
	return factors

def distinctPrimeFactors(n,primos):
	factors = set()
	dividendo = n
	while dividendo > 1:
		for i in range(0,len(primos)):
			if dividendo % primos[i] == 0:
				factors.add(primos[i])
				dividendo = dividendo // primos[i]
				break
	return factors

if __name__ == '__main__':
	primos = getPrimes(200000)
	i = 130000
	encontrado = False
	res = -1
	while not encontrado:
		for j in range(0,4):
			factores = len(distinctPrimeFactors(i,primos))
			if factores != 4:
				break
			else:
				i += 1
		else:
			encontrado = True
			res = i-4
		i += 1
	print(res)
	for i in range(0,4):
		print(distinctPrimeFactors(res+i,primos))