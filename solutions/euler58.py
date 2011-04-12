#euler58
import primes
import itertools as it
import sys

def spiral(n):
	sum = 1
	for side in range(2,n,2):
		for corner in range(4):
			sum += side
			yield sum,side+1

def prime_percent(n):
	prime_count = 0
	percent = 1
	for i,(s,side) in it.izip(it.count(2),spiral(n)):
		if primes.is_prime(s):
			prime_count += 1
			percent = (prime_count*1.0)/i
		percent = (prime_count*1.0)/i
		if percent < .1:
				#print i,percent,side
				print side
				break

if __name__=="__main__":
	primes.init(10**6)
	n = 10**6
	if len(sys.argv) > 1:
		n = eval(sys.argv[1])
	prime_percent(n)
