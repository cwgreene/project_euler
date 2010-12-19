import math

mdivisors = {}
def divisors(n):
	if n in mdivisors:
		return mdivisors[n]
	mdivisors[n] = set()
	for i in xrange(1,int(math.sqrt(n))+1):
		if n % i==0:
			mdivisors[n].add(i)
			mdivisors[n].add(n/i)
	return mdivisors[n]
