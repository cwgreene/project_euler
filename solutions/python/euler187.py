#Problem 187
#
#So, how many options does 2 have? It can be paired with all primes
#less than 10**8/2. How many options does 3 have? All primes less
#than 10**8/3, and greater than 2 (already counted 6). This continues
#up until we hit 10**4, when all will have been accounted for.
#Unfortunately, this isn't quite all primes pairs, and it does really look
#like we need to get all primes less than 100 million, no other way
# to know it seems.
#
#So, assuming we have an array with all primes less than 100 million
#(roughly 10 million I believe), how do we quickly find the reduced 
#multiples? I'm not going to bother actually. I'm just going to run
#through it. It'll be slow at first, but the difference between
#6th and the 7th smallest isn't that big, and we're just iterating
#through the array downwards, so the entire algorithm will be O(n)
#(roughly, not paying to much attention)

import math

import primes

def down_count(prime_array):
	total = 0
	index_left = 0
	index_right = len(prime_array)-1
	while index_left <= index_right: 
		if ((prime_array[index_left]*
		     prime_array[index_right]) <= 10**8):
			total += index_right-index_left+1
			print "total",total
			index_left +=1
		else:
			index_right -= 1
	return total

if __name__=="__main__":
	print "Beginning Count!"
	primes.init(10**8/2)
	print down_count(primes.primes_array)
