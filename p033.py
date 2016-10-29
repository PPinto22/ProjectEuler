def gcd(a,b):
	ab = sorted([a,b])
	a = ab[1]
	b = ab[0]
	divisor = b
	resto = a%b
	while resto != 0:
		dividendo = divisor
		divisor = resto
		resto = dividendo % divisor
	return divisor

def fractions(a,b):
	mdc = gcd(a,b)
	fracs = list()
	reduzida = (a//mdc,b//mdc)
	for i in range(mdc-1,0,-1):
		fracs.append( (reduzida[0]*i,reduzida[1]*i,a/(reduzida[0]*i)) )
	return fracs

def cut(a,b,c,d):
	a = str(a)
	b = str(b)
	c = str(c)
	d = str(d)
	if len(c) > 1 or len(d) > 1:
		return -1
	a0 = a[0]
	if a0 == a[1]:
		if a0 in b:
			b0 = b[0]
			if b0 == b[1]:
				if c[0] == d[0] == a0 == b0:
					return float(a0)
			else:
				if c[0] == a0 and d[0] != b0:
					return float(a[0])
	for i in range(0,2):
		ai = a[i]
		if ai in b and ai not in c and ai not in d and c in a and d in b:
			return float(ai)
	return -1

if __name__ == '__main__':
	res = []
	for dividendo in range(10,99):
	 	for divisor in range(dividendo+1,100):
	 		fracs = fractions(dividendo,divisor)
	 		for (a,b,d) in fracs:
	 			_cut = cut(dividendo,divisor,a,b)
	 			if _cut > 0 and cut != d:
	 				res.append( (dividendo,divisor,a,b) )
	_a = 1
	_b = 1
	_c = 1
	_d = 1
	for (a,b,c,d) in res:
		_a *= a
		_b *= b
		_c *= c
		_d *= d
	print("{a}/{b} = {c}/{d}".format(a=_a,b=_b,c=_c,d=_d))
	print("Simplificado >> {a}/{b}".format(a=_a//gcd(_a,_b),b=_b//gcd(_a,_b)))