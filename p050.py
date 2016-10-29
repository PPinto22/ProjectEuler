# Consecutive prime sum

from p010 import getPrimes
from collections import deque

def maxSequence(p,primes):
	seq = deque()
	_sum = 0
	_max = 0
	i = 0
	while i < len(primes) and primes[i] <= p//2+1:
		_sum += primes[i]
		seq.append(primes[i])
		while _sum > p:
			_sum -= seq.popleft()
		if _sum == p:
			if len(seq) > _max:
				_max = len(seq)
		i += 1
	return _max

if __name__ == '__main__':
	_maxp = -1
	_maxs = -1
	primes = getPrimes(1000000)
	for p in primes:
		print(p)
		s = maxSequence(p,primes)
		if s > _maxs:
			_maxp = p
			_maxs = s
	print(str(_maxp) + ": " + str(_maxs))
