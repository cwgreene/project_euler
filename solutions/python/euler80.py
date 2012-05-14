import decimal 
import math
decimal.getcontext().prec = 200

def sum_digits(dec,k):
	sum = 0
	digits = filter(lambda x: x !='.', str(dec))
	for x in digits[:k]:
		if x != '.':
			sum += int(x)
	return sum

sum = 0 
for x in range(1,100+1):
	if int(math.sqrt(x)) != math.sqrt(x):
		sum += sum_digits(decimal.Decimal(x).sqrt(),100)
print sum
