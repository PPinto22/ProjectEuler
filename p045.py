# Triangular, pentagonal, and hexagonal

def triangleSet(n):
	pl = set()
	for i in range(1,n+1):
		p = int(i*(i+1)/2)
		pl.add(p)
	return pl

def pentagonalSet(n):
	pl = set()
	for i in range(1,n+1):
		p = int(i*(3*i-1)/2)
		pl.add(p)
	return pl

def hexagonalSet(n):
	pl = set()
	for i in range(1,n+1):
		p = int(i*(2*i-1))
		pl.add(p)
	return pl

if __name__ == '__main__':
	ts = triangleSet(100000)
	ps = pentagonalSet(100000)
	hs = hexagonalSet(100000)
	for t in ts:
		if t in ps and t in hs:
			print(t)
