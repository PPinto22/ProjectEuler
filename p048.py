# Self powers

if __name__ == '__main__':
	_sum = 0
	for i in range(1,1001):
		_sum += i**i
	_sum = str(_sum)
	comp = len(_sum)
	print( _sum[comp-10:] )