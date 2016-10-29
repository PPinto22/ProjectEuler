def elimMultiples(dic, key):
	num = key
	while num in dic:
		dic[num] = False
		num += key

def primes(limit):
	dic = {}
	for i in range(2,limit+1):
		dic[i] = True
	for num in dic:
		if(dic[num]):
			elimMultiples(dic, num)
			yield num

def getPrimes(limit):
	lista = []
	for p in primes(limit):
		lista.append(p)
	return lista

def getPrimesSet(limit):
	lista = set()
	for p in primes(limit):
		lista.add(p)
	return lista

def isPrime(N):
	for i in range(2,(abs(N)//2)+1):
		if N % i == 0:
			return False
	return True

if __name__ == '__main__':
	sum = 0
	for p in primes(2000000):
		print(p)
		sum += p
	print("Soma: " + str(sum))