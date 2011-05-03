import math
import numpy as np
parray = np.arange(0,0)
primes_list = []
primes_array = []
primes_set = set();
num_primes = 0
init_primes = False

print "primes alloc!"

def get_primes():
	global parray,primes_list,primes_array,primes_set
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
	primes_array= np.array(primes_list)
	primes_set = set(primes_list)

def init(n):
	global parray,init_primes
	parray = np.arange(0,n)
	get_primes()
	init_primes = True
	print "primes found!"

def sqrt_prime(x):
	max = int(math.sqrt(x))
	if x % 2 == 0:
		return False
	for i in range(3,max+1,2):
		if x % i == 0:
			return False
	return True

def is_prime(x):
	if x < len(parray):
		return (parray[x] != 0)	
	#return sqrt_prime(x)
	return miller_rabin(x)

#not needed
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

#below is good up to
#some num
def miller_rabin(n):
	n = int(n)
	for x in [2L,3L,5L,7L,11L,13L,17L]:
		if pow(x,n-1,n) != 1:
			return False
	return True

def concat_nums(a,b):
	return int(str(a)+str(b))
	#res = a*10**(np.floor(np.log10(b))+1)+b
	
def euler_phi_factors(factors):
	counts = {}
	for p in factors:
		if p in counts:
			counts[p]+=1
		else:
			counts[p]=1
	ep = 1
	for p in counts:
		ep*=(p-1)*p**(counts[p]-1)
	return ep
	

def euler_phi(n, meuler_phi={1:1}):
	if n in meuler_phi:
		return meuler_phi[n]
	if n in primes_set:
		meuler_phi[n] = n-1
		return n-1
	if n < len(parray):
		cur_n = n
		for p in primes_list:
			count = 0
			while cur_n % p == 0:
				count +=1
				cur_n = cur_n/p
			if count > 0:
				if n == p**count:
					result = (p-1)*p**(count-1)
				else:
					result = ((p-1)*p**(count-1)*
						euler_phi(n/p**count))
				meuler_phi[n] = result
				return result
	print "oops!"

