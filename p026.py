def maxCiclo(num):
	restos = []
	resto = 1%num
	restos.append(resto)
	for j in range(1,num):
		resto = (resto*10) % i
		if resto == 0: 
			return 0
		if resto in restos:
			return j
		restos.append(resto)

if __name__ == '__main__':
	_max = 0
	_maxi = -1
	for i in range(2,1000):
		ciclo = maxCiclo(i)
		if ciclo > _max:
			_max = ciclo
			_maxi = i
	print("1/{i} >> ciclo de comprimento {n}".format(i=_maxi,n=_max))		

