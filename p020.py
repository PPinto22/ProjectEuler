def fact(n):
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

def sumDigits(n):
	_sum = 0
	for char in str(n):
		_sum += int(char)
	return _sum
	
if __name__ == '__main__':
	print( sumDigits( fact(100) ) )