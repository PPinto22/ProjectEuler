# Champernowne's constant

if __name__ == '__main__':
	s = ""
	i = 1
	while len(s) < 1000000:
		s += str(i)
		i += 1
	d1 = int(s[0])
	d10 = int(s[9])
	d100 = int(s[99])
	d1000 = int(s[999])
	d10000 = int(s[9999])
	d100000 = int(s[99999])
	d1000000 = int(s[999999])
	print(d1*d10*d100*d1000*d10000*d100000*d1000000)