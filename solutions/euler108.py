from fractions import Fraction as Frac
from common_funcs import gcd

def reciprocals(n):
	x = n+1
	result = []
	while Frac(1,n)-2*Frac(1,x) <= 0:
		diff = Frac(1,n)-Frac(1,x)
		if diff.numerator == 1:
			result.append((x,diff.denominator))
			print len(result)
		x+=1
	return result
nums = [2*3*5*7*11*13*6]
for x in nums:
	res = reciprocals(x)
	print len(res),x
