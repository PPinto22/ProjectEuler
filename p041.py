# Pandigital prime

from p032 import pandigital
from p024 import permutations
from p010 import isPrime

if __name__ == '__main__':
	# Por tentativa e erro, para n=8 ou n=9, nao houve primos
	pandigitals9 = permutations(['1','2','3','4','5','6','7']) 
	s = sorted(pandigitals9)
	_max = -1
	for i in range(len(s)-1,0,-1):
		num = int(s[i])
		print(num)
		if(isPrime(num)):
			_max = num
			break
	print("\nMaximo >> " + str(_max))