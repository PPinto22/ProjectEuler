def alphaValue(name):
	name = name.lower()
	value = 0
	for char in name:
		value += ord(char)-96
	return value

if __name__ == '__main__':
	with open('p022_names.txt', 'r') as myfile:
	    data = myfile.read()

	names = data.replace("\"","")
	names = names.split(",")

	i = 1
	total = 0
	for name in sorted(names):
		total += i*alphaValue(name)
		i += 1

	print(total)
