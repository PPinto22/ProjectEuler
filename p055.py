def palindrome(n1):
	return str(n1) == str(n1)[::-1]

def reverse(n):
	return int( str(n)[::-1] )

def isLychrel(n):
	n = n + reverse(n)
	for i in range(1,50):
		if palindrome(n):
			return False
		n = n + reverse(n)
	return True

if __name__ == '__main__':
	lychrels = list()
	for i in range(0,10000):
		if isLychrel(i):
			lychrels.append(i)
	print(len(lychrels))