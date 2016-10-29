from p010 import getPrimesSet

def truncatable(prime,primeTestFunction):
	prime = str(prime)
	for i in range(1,len(prime)):
		if not primeTestFunction(int(prime[i:])):
			return False
		if not primeTestFunction(int(prime[:i])):
			return False
	return True
	
if __name__ == '__main__':
	_set = getPrimesSet(1000000)
	eleven = list()
	for p in _set:
		if truncatable(p,lambda x: x in _set):
			eleven.append(p)
	eleven.remove(2)
	eleven.remove(3)
	eleven.remove(5)
	eleven.remove(7)
	print(eleven)
	print(sum(eleven))