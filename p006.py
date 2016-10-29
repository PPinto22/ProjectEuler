def sumSquares(N):
	sum = 0
	for i in range(1,N+1):
		sum += i**2
	return sum

def squareSum(N):
	return sum(range(1,N+1))**2

NUMBER = 100
_sum = sumSquares(NUMBER)
_square = squareSum(NUMBER) 
print("Sum of the squares: " + str(_sum))
print("Square of the sum: " + str(_square))
print("Diferenca: " + str(_square - _sum))