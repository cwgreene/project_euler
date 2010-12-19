def digits(x):
	return map(int,str(x))
	
def from_digits(digits_list):
	power = 1
	sum = 0
	for x in reversed(digits_list):
		sum +=x*10**power
	return sum
