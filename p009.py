
def pythag():
	for a in range(1,500):
		#print("a = {a}".format(a=a))
		for b in range(1,500):
			for c in range(1,500):
				if ( (a + b + c == 1000) and (a**2 + b**2 == c**2) ):
					return (a,b,c)

triplo = pythag()
a = triplo[0]
b = triplo[1]
c = triplo[2]
print("a = {0}, b = {1}, c = {2}".format(a,b,c))
print("a*b*c = {0}".format(a*b*c))