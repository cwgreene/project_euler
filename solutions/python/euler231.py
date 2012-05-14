#sum of prime factors of 
#20*10**6, 15*10**6
import numpy as np
import primes

def somewhat_smaller_binom(n,k):
	z = np.arange(k,n+1)
	#for i in np.arange(2,(n-k)+1):
	z[:-2] /= np.arange(2,(n-k)+1)
	
	map(primes.factor,z)

primes.init(10**7)
print somewhat_smaller_binom(20*10**6,15*10**6)
