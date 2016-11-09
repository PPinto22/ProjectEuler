from math import factorial

def c(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))

def main():
	count = 0
	for n in range(1,101):
		for r in range(1,n+1):
			cnr = c(n,r)
			if cnr > 1000000:
				count += 1
	print(count)

if __name__ == '__main__':
	main()