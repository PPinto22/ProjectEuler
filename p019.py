def isLeap(year):
	return (year%4 == 0) and (year%100 != 0 or year%400 == 0)

dias = 366 #dias desde 1 Jan 1900 (segunda)
segundas = 0
for year in range(1901,2000+1):
	#Jan
	if dias % 7 == 0:
		segundas += 1
	dias += 31

	#Fev
	if dias % 7 == 0:
		segundas += 1
	if isLeap(year):
		dias += 29
	else:
		dias += 28
		
	#Marco
	if dias % 7 == 0:
		segundas += 1
	dias += 31

	#Abril
	if dias % 7 == 0:
		segundas += 1
	dias += 30

	#Maio
	if dias % 7 == 0:
		segundas += 1
	dias += 31

	#Junho
	if dias % 7 == 0:
		segundas += 1
	dias += 30

	#Julho
	if dias % 7 == 0:
		segundas += 1
	dias += 31

	#Agosto
	if dias % 7 == 0:
		segundas += 1
	dias += 31

	#Setembro
	if dias % 7 == 0:
		segundas += 1
	dias += 30

	#Outubro
	if dias % 7 == 0:
		segundas += 1
	dias += 31

	#Novembro
	if dias % 7 == 0:
		segundas += 1
	dias += 30

	#Dezembro
	if dias % 7 == 0:
		segundas += 1
	dias += 31

print(segundas)