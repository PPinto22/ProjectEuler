res = []

for num in range(10,200000):
	_sum = 0
	for digit in str(num):
		_sum += int(digit)**5
	if(_sum == num):
		res.append(num)

print(res)
print(sum(res))