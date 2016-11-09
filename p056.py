def digitalSum(n):
	_sum = 0
	for digit in str(n):
		_sum += int(digit)
	return _sum

if __name__ == '__main__':
	_max = 0
	_a = 0
	_b = 0
	for a in range(1,100):
		for b in range(1,100):
			_sum = digitalSum(a**b)
			if _sum > _max:
				_max = _sum
				_a = a
				_b = b
	print("a = " + str(a) + ", b = " + str(b))
	print(_max)
	