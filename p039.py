# Integer Right Triangles
#
#   |\
# b | \ c
#   |__\
#    a

import math

def solucoesPorP(p):
	solucoes = set()
	for a in range(1,p):
		for b in range(1,p-a):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == float(p):
				sol = frozenset([a,b,int(c)])
				solucoes.add(sol)
				break
			if a + b + c > p:
				break
	return solucoes

if __name__ == '__main__':
	_max = set()
	_maxp = -1
	for p in range(3,1001):
		print(p)
		solucoes = solucoesPorP(p)
		if len(solucoes) > len(_max):
			_max = solucoes
			_maxp = p
	print(_max)
	print(len(_max))
	print(_maxp)

