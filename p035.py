from p010 import getPrimesSet

def rotations(number):
	number = str(number)
	_set = set()
	for i in range(0,len(number)):
		_set.add(int(number[i:] + number[:i]))
	return _set

if __name__ == '__main__':
	primeSet = getPrimesSet(1000000)
	_result = set()
	for prime in primeSet:
		if all(rotation in primeSet for rotation in rotations(prime)):
			_result.add(prime)
	print(sorted(_result))
	print(len(_result))


