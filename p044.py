# Pentagon numbers
# Pn=n(3n−1)/2

def pentagonalSet(n):
	pl = set()
	for i in range(1,n+1):
		p = int(i*(3*i-1)/2)
		pl.add(p)
	return pl

if __name__ == '__main__':
	pl = pentagonalSet(10000)
	_min = 999999999999999
	_j = 0
	_k = 0
	for j in pl:
		for k in pl:
			_sum = j+k
			if _sum in pl:
				_diff = k-j
				if _diff in pl and _diff < _min:
					print("* j = {0}, k = {1}, diff = {2}".format(j,k,_diff))
					_min = _diff
					_j = j
					_k = k
	print("j = {0}, k = {1}, diff = {2}".format(_j,_k,_min))

