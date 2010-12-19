import math
array = range(0,10**8+1)
primes = []
twice_squares = range(0,10**6+1)
def get_primes():
	global array,primes
	i = 4
	cur_prime = 2
	array_length = len(array)
	sq_array_length = int(math.sqrt(len(array)))
	while i < sq_array_length:
		i = cur_prime*2
		while i < array_length:
			array[i] = 0
			i+= cur_prime
		i = cur_prime+1
		while i < sq_array_length:
			if array[i] != 0:
				cur_prime = array[i]
				break
			i+=1
	array[0] = 0
	array[1] = 0 #not prime
	for x in array:
		if x != 0:
			primes.append(x)

def get_twice_squares():
	for i in xrange(len(twice_squares)):
		twice_squares[i] = 0
	for i in xrange(int(math.sqrt(len(twice_squares)/2))):
		twice_squares[2*i*i]=2*i*i
		

def is_Goldbach_Counterexample(x):
	if x%2 == 0:
		return False
	if array[x]:
		return False
	for p in primes:
		if twice_squares[x-p]:
			return False
	return True
mnum_prime_factors = {}
def num_prime_factors(n):
	count = 0
	if n in mnum_prime_factors:
		return mnum_prime_factors[n]
	for x in primes[0:int(math.sqrt(n))+1]:
		if n % x ==0:
			count +=1
	mnum_prime_factors[n] = count
	return count
if primes == []:
	get_primes()
	#get_twice_squares()
