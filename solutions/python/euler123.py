import primes
from bisect import bisect
from common_funcs import fast_mod_pow as fmp

#really easy to make off by one errors on this one
def main():
	primes.init(10**7)
	pl = primes.primes_list
	start = bisect(pl,10**5)
	print start
	for n,p in enumerate(pl[start:]):
		p = int(p)
		p2 = p**2
		rem = (fmp(p-1,n+1+start,p2)+fmp(p+1,n+1+start,p2) )% p2 
		if rem > 10**10:
			break
	print p,rem,n+start+1
main()
