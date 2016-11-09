from p010 import getPrimesSet, getPrimes

def countPrimes(conjunto,primos):
	count = 0
	for num in conjunto:
		if num in primos:
			count += 1
	return count

def combinationsRec(length,ndigits,ciclos,ciclo):
	comb = list()
	if ciclo == ndigits:
		lista = list()
		for c in ciclos:
			lista.append(c)
		comb.append(lista)
	else:
		if ciclo == 0:
			start = 0
		else:
			start = ciclos[ciclo-1]+1
		for i in range(start,length-ndigits+ciclo+1):
			ciclos[ciclo] = i
			comb += combinationsRec(length,ndigits,ciclos,ciclo+1)
	return comb

def indexCombinations(length,ndigits):
	ciclos = list()
	for i in range(0,ndigits):
		ciclos.append(i)
	return combinationsRec(length,ndigits,ciclos,0)

def replacementsN(num,ndigits,matriz):	
	#cind = indexCombinations(len(num),ndigits)
	cind = matriz[(len(num),ndigits)]
	for indices in cind:
		conjunto = set()
		for d in range(0,10):
			aux = list(''.join(num))
			ok = True
			for indice in indices:
				if d == 0 and indice == 0:
					ok = False
				else:
					aux[indice] = str(d)
			if ok:
				conjunto.add(int(''.join(aux)))
		yield conjunto

def replacements(num,matriz):
	num = list(str(num))
	for ndigits in range(1,len(num)):
		for conjunto in replacementsN(num,ndigits,matriz):
			yield conjunto

def main():
	primos = getPrimesSet(1000000)

	matriz = dict()
	for length in range(0,7):
		for ndigits in range(1,length):
			matriz[(length,ndigits)] = indexCombinations(length,ndigits)

	#for i in range(0,1000000):
	for i in sorted(primos):
		for conjunto in replacements(i,matriz):
			count = countPrimes(conjunto,primos)
			if count == 8:
				print(conjunto)
				print(sorted(conjunto)[0])
				return 

		print(i)

if __name__ == '__main__':
	main()
