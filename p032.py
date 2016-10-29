def pandigital(n):
	num = str(n)
	for digit in num:
		if digit == '0' or num.count(digit) > 1:
			return False
	return True

if __name__ == '__main__':
	prod_set = set()
	for a in range(0,100):
		if pandigital(a):
			for b in range(0,2000):
				prod = a*b
				if prod not in prod_set:
					mmp = int(str(a) + str(b) + str(prod))
					str_mmp = str(mmp)
					if len(str_mmp) == 9 and pandigital(mmp):
						prod_set.add(prod)
	print(prod_set)
	print(sum(prod_set))
