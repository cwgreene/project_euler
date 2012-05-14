import primes
import common_funcs as cfn
import math

#eh, pair method,
#not guaranteed to work
def find_perms():
	primes.init(10**7)
	big_primes = [p for p in reversed(primes.primes_list)]
	min = 10**7
	minval = 10**7
	start = cfn.binary_search(primes.primes_list,
			math.sqrt(10**7),
			len(primes.primes_list)-1,0)
	print start
	big_primes = [p for p in reversed(primes.primes_list[:start+1])]
	for p in big_primes:
		for bp in reversed(big_primes):
			if bp > p:
				break
			for bp2 in reversed(big_primes):
				if bp2 > bp:
					break
				print p,bp,bp2
				comp = int(p)*int(bp)*int(bp2)
				ep = int(p-1)*int(bp-1)*int(bp2-1)
				if comp/(ep*1.) >= minval:
					break
				if (cfn.digit_hash(comp)==cfn.digit_hash(ep) 
					and comp/(ep*1.) < minval):
					min = comp
					minval = comp/(ep*1.)
					print comp,p,bp,bp2,ep,comp/(ep*1.)
					break #biggest for this p

#guaranteed to work
#turns out answer only uses 2 primes
def brute_force():
	cands = range(10**6,10**7)
	for i,x in enumerate(cands):
		ep = primes.euler_phi(x)
		cands[i] = x,ep,x/(1.*ep)
	print "eulerphi computed"
	cands.sort(key=lambda x:x[2])
	print "sorted"
	for cand in cands:
		if cfn.digit_hash(cand[0])==cfn.digit_hash(cand[1]):
			print cand
			break
def find_primes(n):
	#for a given prime n, the best for that prime will be
	#the largest number. so once you found one, you can stop
	pass

def main():
	primes.init(10**7)
	brute_force()

if __name__=="__main__":
	main()
