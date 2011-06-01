#okay, so we compute eulerphi for 10^8
#to get the size of the group.
#since b^a mod k = b^(a mod phi(k)) mod k
#we can compute this fairly easily
import primes
import sys
primes.init(10**6)
sys.setrecursionlimit(2000)
def hyperexponent_mod(n,k,mod):
	stack = []
	acc = n
	while k != 1:
		phi = primes.euler_phi(mod,ignore=True)
		stack.append((phi,mod))
		mod = phi
		k-=1
	stack.reverse()
	#print stack
	for phi,mod in stack:
		acc = pow(n,acc%phi,phi)
	return acc%mod
	
def hyperexponent_mod_rec(n,k,mod):
	if k ==1:
		return n%mod
	phi = primes.euler_phi(mod,ignore=True)
	return pow(n,hyperexponent_mod_rec(n,k-1,mod),mod)%mod


print hyperexponent_mod_rec(3,3,10**8)
print hyperexponent_mod_rec(1777,1855,10**8)
print hyperexponent_mod(1777,1855,10**8)
