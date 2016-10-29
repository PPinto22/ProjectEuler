from p022 import alphaValue

def triangleSet(N):
	tris = set()
	for i in range(1,N+1):
		tris.add(int(1/2*i*(i+1)))
	return tris

if __name__ == '__main__':
	with open('p042_words.txt', 'r') as myfile:
	    data = myfile.read()
	names = data.replace("\"","")
	names = names.split(",")

	count = 0
	tris = triangleSet(20)
	for name in names:
		valor = alphaValue(name)
		if valor in tris: count += 1
	print(count)