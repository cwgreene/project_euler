#this should work, but 10^6+171 doesn't work
#That's because you forgot about zero-divisors

import primes
from Queue import PriorityQueue
from common_funcs import gcd


#below was a nice idea
"""
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
"""

#brute force the damn things
def handle_zero_divisors(n):
	#perform sum
	count =0
	acc = 1
	sum = 1 
	while sum != 0:
		acc = (acc*10) % n
		sum = (sum+acc) % n
		count +=1
	return count

def smallest_k(n,min=0):
	if gcd(n,10) != 1:
		return None
	if gcd(n-9,n) != 1:
		res = handle_zero_divisors(n)
		print n,res
		return res
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
	#A(n) < n. Apparently, the pigeonhole principle can be pulled out
	#but I'm a bit confused as to how, as the number of states
	#the sum can be in is dependent not only on the current sum
	#but also the number of possible increments. Both of these 
	#potentially are n, so it seems the A(n) is only bounded by n^2.
	#for non-zero divisors, this can be immediately shown.
	k = 10**6-1
	small = None
	while small == None:
		k+=2
		if k % 5 == 0:
			k+=2
		small = smallest_k(k)
		if small < max:
			small = None
	print k
main(10**6)
