def spell(digit):
	if digit == 1:
		return "one"
	elif digit == 2:
		return "two"
	elif digit == 3:
		return "three"
	elif digit == 4:
		return "four"
	elif digit == 5:
		return "five"
	elif digit == 6:
		return "six"
	elif digit == 7:
		return "seven"
	elif digit == 8:
		return "eight"
	elif digit == 9:
		return "nine"

def spellTens(tens, units):
	if tens == 1:
		if units == 0:
			return "ten"
		elif units == 1:
			return "eleven"
		elif units == 2:
			return "twelve"
		elif units == 3:
			return "thirteen"
		elif units == 4:
			return "fourteen"
		elif units == 5:
			return "fifteen"
		elif units == 6:
			return "sixteen"
		elif units == 7:
			return "seventeen"
		elif units == 8:
			return "eighteen"
		elif units == 9:
			return "nineteen"
	elif tens == 2:
		if units == 0:
			return "twenty"
		else:
			return "twenty-"+spell(units)
	elif tens == 3:
		if units == 0:
			return "thirty"
		else:
			return "thirty-"+spell(units)
	elif tens == 4:
		if units == 0:
			return "forty"
		else:
			return "forty-"+spell(units)
	elif tens == 5:
		if units == 0:
			return "fifty"
		else:
			return "fifty-"+spell(units)
	elif tens == 6:
		if units == 0:
			return "sixty"
		else:
			return "sixty-"+spell(units)
	elif tens == 7:
		if units == 0:
			return "seventy"
		else:
			return "seventy-"+spell(units)
	elif tens == 8:
		if units == 0:
			return "eighty"
		else:
			return "eighty-"+spell(units)
	elif tens == 9:
		if units == 0:
			return "ninety"
		else:
			return "ninety-"+spell(units)

def words(number):
	if number == 1000: 
		return "one thousand"
	else:
		hundreds = number//100
		tens = (number - hundreds*100)//10
		units = number - 100*hundreds - 10*tens
		string = ""
		if hundreds > 0:
			string = string + spell(hundreds) + " hundred"
			if tens > 0:
				string = string + " and " + spellTens(tens,units)
			elif units > 0:
				string = string + " and " + spell(units)
		else:
			if tens > 0:
				string = spellTens(tens,units)
			elif units > 0:
				string = spell(units)
			else: string = "zero"
		return string

letters = 0
for i in range(1,1000+1):
	string = words(i)
	string = string.replace(" ","").replace("-","")
	#print("{0} -> {1}".format(i,string))
	letters += len(string)

print("Total de letras >> {0}".format(letters))