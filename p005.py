def divisible(target,N):
	if (N == 0 | N == 1):
		return True
	elif target % N == 0:
		return divisible(target,N-1)
	else:
		return False
	
solution = 1
while True:
	if divisible(solution,20):
		print("Menor numero divisivel por 1..20: " + str(solution))
		break
	else:
                print("Nop... " + str(solution))
                solution += 1
