def chain(_number):
	n = _number
	elems = 1
	while n != 1:
		elems += 1
		if n % 2 == 0:
			n = n//2
		else:
			n = 3*n + 1
	return elems

_max = 0
_number = -1
for i in range(1,1000000):
	aux = chain(i)
	if i%10000 == 0:
		print("{0} ---> {1}".format(i,aux))
	if aux > _max:
		_max = aux
		_number = i
print("Maximo: {0} ---> {1}".format(_number,_max))