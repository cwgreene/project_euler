import primes

def main(n):
	primes.init(10**6)
	nums = [1,3,7,9,13,27]
	offnums = [11,17,19,21,23]
	total = 0
	failure = False
	#below is the only intelligent part
	#look at each of the numbers modulo 5
	#and we can eliminate all possibilities for
	#n^2 except for n mod 5 = 0.
	for x in xrange(10,n,10):
		square = x*x
		if (((x % 3) not in (1,2)) 
			or ((x % 7) not in (3,4))):
			continue
		for offset in nums:
			if not primes.is_prime(square+offset):
				failure = True
				break
		if failure:
			failure = False
			continue
		for offset in offnums:
			if primes.is_prime(square+offset):
				failure = True
				break
		if not failure:
			print "Yay",x
			total += x
		failure = False
	print total
main(10*10**6)
