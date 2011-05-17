#this should work, but 10^6+171 doesn't work
#That's because you forgot about zero-divisors

import primes
from common_funcs import gcd

def handle_zero_divisors(n):
	print "Zero divisors"

def smallest_k(n,min=0):
	if gcd(n,10) != 1:
		return None
	if gcd(n-9,n) != 1:
		return handle_zero_divisors(n)
	factors = primes.all_factors(primes.factor(primes.euler_phi(n)))
	if factors[-1] < min:
		return None
	for factor in factors:
		factor = int(factor)
		if pow(10,factor,n) == 1:
			if factor < min:
				return None
			return factor

def main(max):
	primes.init(2*10**6+1)
	k = max+1
	small = None
	while small == None:
		k+=2
		if k % 5 == 0:
			k+=2
		small = smallest_k(k)
		if small < max:
			small = None
	print k
	print sum([len(primes.all_factors(primes.factor(
		primes.euler_phi(k)))) +1 for k 
		  in range(10**6,10**6+171+1)])
main(10**6)
