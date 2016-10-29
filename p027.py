from p010 import getPrimes
from p007 import isPrime

rangeB = getPrimes(1000)
negativos = []
for p in rangeB:
	negativos.append(-p)
rangeB = negativos + rangeB

_maxA = -1
_maxB = -1
_maxPrimos = 0

for a in range(-999,1000):
	if a % 100 == 0:
		print("a = {0}... ".format(a),end="",flush=True)
	for b in rangeB:
		sequencia = True
		n = 0
		while sequencia:
			if isPrime(n**2 + a*n + b):
				n += 1
			else:
				sequencia = False
		if n > _maxPrimos:
			_maxPrimos = n
			_maxA = a
			_maxB = b

print("\na = {a}\nb = {b}\nprimos = {p}\na * b = {ab}".format(a=_maxA,b=_maxB,p = _maxPrimos,ab=_maxA*_maxB))