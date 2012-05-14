from fractions import Fraction as Frac
from common_funcs import gcd,choose_degen,choose
import primes

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

def product(alist):
	p = 1
	for a in alist:
		p*=a
	return p

def pyramid_enumerate(n,options,f):
	result = []
	index = 0
	for i in range(n):
		while (f(result+[options[index]]) < 
			f(result+[options[index+1]])):
			print index
			index += 1
		result.append(options[index])
		index = 0
	return result

def combinations_distinct(alist):
	total = 0
	for x in range(1,len(alist)+1):
		total += choose_degen(alist,x)*2**(x-1)
	return total+1

primes.init(1000)

nums = [2*3*2*3*5*5]
for x in nums:
	res = reciprocals(x)
	print res,map(lambda x: Frac(x[1])/Frac(x[0]),res)
	print len(res),x
	print combinations_distinct([(2,2),(3,2),(5,2)])
