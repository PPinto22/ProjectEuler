found = False
x = 0
while not found:
	x += 1
	for m in range(2,7):
		smx = str(m*x)
		sx = str(x)
		if len(sx)!=len(smx) or not all(sx.count(digit) == smx.count(digit) for digit in sx):
			break
	else:
		found = True

for i in range(1,7):
	print(str(i) + " * " + str(x) + " = " + str(i*x))