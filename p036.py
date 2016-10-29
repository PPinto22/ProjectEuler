def palindrome(s):
	for i in range(0,len(s)//2):
		if s[i] != s[len(s)-1-i]:
			return False
	return True

def decToBin(n):
	return "{0:b}".format(n)

if __name__ == '__main__':
	res = list()
	for i in range(0,1000000):
		if palindrome(str(i)) and palindrome(decToBin(i)):
			res.append( i )
	print(res)
	print(sum(res))
