from p021 import properDivisors 

def isAbundantNumber(n):
	return sum(properDivisors(n)) > n

def isSumOfAbundantNumbers(n,abundants):
	abund = abundants[0]
	i = 0
	while i < len(abundants) and n > abund:
		abund = abundants[i]
		difference = n - abund
		if difference in abundants:
			return True
		i += 1
	return False

if __name__ == '__main__':
	abundants = []
	print("Calculating abundant numbers... ", end="", flush=True)
	for i in range(1,28123+1):
		if i%5000 == 0:
			print("{0}... ".format(i), end="", flush=True)
		if isAbundantNumber(i):
			abundants.append(i)
	print("OK")

	_sum = 0
	print("Finding integers which cannot be writen as the sum of two abundant numbers... ")
	# Ultimo num que nao e a soma de dois abundantes > 20161 (?)
	for i in range(1,28123+1):
		if not isSumOfAbundantNumbers(i,abundants):
			print("{0} >> No".format(i))
			_sum += i
		else:
			print("{0} >> Yes".format(i))
	print("Sum >> "+str(_sum))


