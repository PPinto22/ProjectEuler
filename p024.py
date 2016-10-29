def permutations(lista):
	if len(lista) <= 1: return lista
	conjunto = set()
	for digito in lista:
		sub_lista = list(lista)
		sub_lista.remove(digito)
		subconjunto = permutations(sub_lista)
		for combinacao in subconjunto:
			conjunto.add(digito + combinacao)
	return conjunto

if __name__ == '__main__':
	digitos = ['0','1','2','3','4','5','6','7','8','9']
	print( sorted(permutations(digitos))[999999] )