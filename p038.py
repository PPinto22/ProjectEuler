from p032 import pandigital
	
if __name__ == '__main__':
	_max = 0
	_maxi = -1
	_maxn = -1
	for i in range(1,10000):
		product = ""
		for n in range(1,10):
			product += str(i*n)
			if not '0' in product and len(product) == 9 and pandigital(int(product)):
				if int(product) > _max:
					_max = int(product)
					_maxi = i
					_maxn = n
			if len(product) >= 9:
				break
	print(str(_maxi) + " * " + str(range(1,_maxn,1)))
	print(_max)