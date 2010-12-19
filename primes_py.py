import math
parray = range(2*10**6)
primes_list = []
num_primes = 0

"""def get_primes():
	global parray,primes_list
	i = 4
	cur_prime = 2
	array_length = len(parray)
	sq_array_length = int(math.sqrt(len(parray)))
	while i < sq_array_length:
		i = cur_prime*2	     #zero next prime
		parray[i::cur_prime] = 0#zero multiples of prime
		i = cur_prime+1
		while i < sq_array_length:
			if parray[i] != 0:
				cur_prime = parray[i]
				break
			i+=1
	parray[0] = 0
	parray[1] = 0 #not prime
	primes_list = parray[parray.nonzero()]

get_primes()"""

def sqrt_prime(x):
	max = int(math.sqrt(x))
	if x % 2 == 0:
		return False
	for i in range(3,max+1,2):
		if x % i == 0:
			return False
	return True

def is_prime(x):
	#return sqrt_prime(x)
	return miller_rabin(x)

def fast_mod_exp(num,exp,b):
	#ensures we never magically become int32
	cur_exp = exp
	res = 1
	#cur_exp is odd
	while cur_exp > 0:
		if cur_exp % 2:
			res = (res*num) % b
		cur_exp /= 2
		num = num*num % b
	return res

def miller_rabin(n):
	n *= 1L
	for x in [2L,3L,5L,7L,11L,13L,17L]:
		if fast_mod_exp(x,n-1,n) != 1:
			return False
	return True
