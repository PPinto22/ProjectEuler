# Sub-string divisibility

from p024 import permutations

def pandigital09(n):
	num = str(n)
	if len(num) != 10:
		return False
	for digit in num:
		if num.count(digit) > 1:
			return False
	return True

def subStringDiv(n):
	num = str(n)
	primos = [2,3,5,7,11,13,17]
	for i in range(1,8):
		subN = int(num[i:i+3])
		if not subN%primos[i-1] == 0:
			return False
	return True

if __name__ == '__main__':
	ps = permutations(list("0123456789"))
	rs = set()
	for p in ps:
		if subStringDiv(p):
			rs.add(int(p))
	print(rs)
	print(sum(rs))