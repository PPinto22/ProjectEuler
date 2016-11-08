from p010 import getPrimesSet

def countPrimes(conjunto,primos):
	count = 0
	for num in conjunto:
		if conjunto in primos:
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

def replacementsN(num,ndigits):
	cind = indexCombinations(len(num),ndigits)
	for d in range(0,10):
		conjunto = set()
		for indices in cind:
			for indice in indices:
				aux = list(''.join(num))
				aux[indice] = str(d)
			conjunto.add(int(''.join(aux)))
		yield conjunto

def replacements(num):
	num = list(str(num))
	for ndigits in range(1,len(num)):
		for conjunto in replacementsN(num,ndigits):
			yield conjunto

if __name__ == '__main__':
	for r in replacements(10):
		print(r)