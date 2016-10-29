def properDivisors(n):
	divs = []
	for i in range(1, (n//2)+1 ):
		if n%i == 0:
			divs.append(i)
	return divs

if __name__ == '__main__':
	d = {}
	print("Calculating proper divisors... ", end="", flush=True)
	for i in range(1,10000+1):
		d[i] = sum(properDivisors(i))

	print("OK")

	soma = 0
	for i in range(1,10000+1):
		if d[i] in d and d[i] != i and d[ d[i] ] == i:
			#Amicable numbers
			print(str(i) + " " + str(d[i]))
			soma += i

	print("The sum of all amicable numbers under 1000 is >> " + str(soma))
