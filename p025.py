def fibonacci():
	fib1 = 1
	fib2 = 1
	yield fib1
	yield fib2
	while True:
		aux = fib2
		fib2 = fib2 + fib1
		fib1 = aux
		yield fib2

i = 1
for fib in fibonacci():
	if len(str(fib)) == 1000:
		print(i)
		print(fib)
		break
	i += 1
