#def routes(i,j,LIMIT_I,LIMIT_J):
#	if i==LIMIT_I and j==LIMIT_J:
#		return 1
#	else:
#		if i == LIMIT_I:
#			return routes(i,j+1,LIMIT_I,LIMIT_J)
#		elif j == LIMIT_J:
#			return routes(i+1,j,LIMIT_I,LIMIT_J)
#		else:
#			return routes(i,j+1,LIMIT_I,LIMIT_J)+routes(i+1,j,LIMIT_I,LIMIT_J)
#
#print("Total de rotas (20x20) >> " + str(routes(0,0,20,20)))

gridSize = 20;
paths = 1;
 
for i in range(0,gridSize):
	paths *= (2*gridSize) - i
	paths //= i+1

print(str(paths))