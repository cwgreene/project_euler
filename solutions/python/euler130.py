#this should work, but 10^6+171 doesn't work
#That's because you forgot about zero-divisors

import primes
from Queue import PriorityQueue
from common_funcs import gcd

def handle_zero_divisors(n):
	print "Zero divisors",
	factors = primes.all_factors(primes.factor(primes.euler_phi(n)))
	possibilities = PriorityQueue()
	for factor in factors:
		factor = int(factor)
		if pow(10,factor,n) == 1:
			possibilities.put((factor,factor,1))
	if possibilities.empty():
		return None
	while True: #should eventually terminate
		_,factor,multiple = possibilities.get()
		if pow(100,factor,n) == 1:
			print n,factor*multiple
			return factor*multiple
		possibilities.put((factor*(multiple*1),factor,multiple+1))


def smallest_k(n,min=0):
	if gcd(n,10) != 1:
		return None
	if gcd(n-9,n) != 1:
		return None
#		return handle_zero_divisors(n)
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
	primes.init(2*max+1)
	k = 89
	results = []
	while len(results) <25:
		k+=2
		if k % 5 == 0:
			k+=2
		if primes.is_prime(k):
			continue
		small = smallest_k(k)
		if small and ((k-1) % small) == 0:
			print small
			results.append(k)
			print results
	print sum(results)
main(10**6)
