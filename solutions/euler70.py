#status: unsolved

#Okay, since euler_phi(p*m)=(p-1)*(m-1)=p*m-(p+m)+1, 

#to get this as close
#to one as possible, we want the -1's to not be that big. 
#if we were to consider a larger product of primes, 
#it seems like this situation would get worse.

import primes
import math

def is_perm_array(x,y):
	xs = str(x)
	ys = str(y)
	if len(xs) != len(ys):
		return false
	xa = [0]*10
	ya = [0]*10
	for i in range(len(xs)):
		xa[i] = xs[i]
		ya[i] = ys[i]
	for i in range(10):
		if xa[i] != ya[i]:
			return False
	return True

def is_perm_prime(x,y):
	xs = map(int,str(x))
	ys = map(int,str(y))
	numx = 1
	numy = 1
	for x,y in zip(xs,ys):
		numx *= primes.primelist[x]
		numy *= primes.primelist[y]

def is_perm(x,y):
	return is_perm_arra(x,y)

def main():
	for prime in primes.primes_list:
		alpha = int(math.log(10**7,prime))
		phi = euler_phi(prime**alpha)
