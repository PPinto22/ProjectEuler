def singleFact(n):
	if n == 0 or n == 1: return 1
	elif n == 2: return 2
	elif n == 3: return 6
	elif n == 4: return 24
	elif n == 5: return 120
	elif n == 6: return 720
	elif n == 7: return 5040
	elif n == 8: return 40320
	elif n == 9: return 362880 

def digitFact(n):
	_sum = 0
	for digit in str(n):
		_sum += singleFact(int(digit))
	return _sum

res = list()
for i in range(3,2500000):
	if digitFact(i) == i:
		res.append(i)
print(res)
print(sum(res))