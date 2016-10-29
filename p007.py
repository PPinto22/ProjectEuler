def primes():
	num = 2
	while True:
		if isPrime(num):
			yield num
		num += 1

def isPrime(N):
	for i in range(2,(abs(N)//2)+1):
		if N % i == 0:
			return False
	return True

if __name__ == '__main__':
	i = 1
	for p in primes():
		if i % 100 == 0:
			print("Prime #" + str(i) + " = " + str(p) + "...")
		if i == 10001:
			print("Prime #" + str(i) + " = " + str(p))
			break
		i += 1
