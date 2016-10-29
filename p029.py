terms = set()

for a in range(2,100+1):
	for b in range(2,100+1):
		terms.add(a**b)

print(len(terms))
