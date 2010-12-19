import math

#this problem can be done by hand.
#Consider the following
#for all fractions in the sequence
#a/b - n/m = 1/(b*m)
#(this can be shown by demonstrating that
#(n/m+1/(b*m) is also in the sequence)

#this means that b*n-a*m = 1
#which gives an expression for m in terms of n
#which means we simply need to find the largest integer
#that satisfies that equation that keeps m < 1,000,000.

#slow way

"""
max = 0
p:for x in range(1,(3*10**6-1)/7+1):
	if (1+7*x) % 3 == 0:
		y = (1+7*x)/3
		if  x > max:
			max = x; n = x; m = y;
print n"""
#(1+7n)/3  < 10**6, solve for n
#(1+7n) must be divisible by 3 so
#7n mod 3 = -1 mod 3
# = (7 mod 3)*(n mod 3) = 1*(n mod 3) = -1 mod 3)
# = n mod 3 = -1 mod 3 == 2 mod 3

#since (3*10**6-1)/7 is the largest integer that
#will let m < 10**6, we can't increase n (add two)
#so we subtract until it's acceptable
"""n = ((3*10**6-1)/7) -1 #largest integer
while n %3 != 2:
	n-=1
m = (1+7*n)/3

print n"""

#the following implementation is too slow
#no need for while_loop

#But we should remove the magic numbers!
def predecessor_slow(a,b,maxsize):
	n = ((a*maxsize-1)/b)
	while (b*n +1)%a != 0:
		n-=1
	m = (1+n*b)/a
	return n,m

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

def find_factor(n):
	for x in range(math.sqrt(n)):
		if n %x == 0:
			return x
	return 1

def prime_factorize(n):
	factors = {}
	rem = n
	while rem != 1:
		found = False
		for x in range(2,int(math.sqrt(rem))+1):
			if rem %x == 0:
				if x in factors:
					factors[x] +=1
				else:
					factors[x] = 1
				rem /= x
				found = True
				break
		if not found:
			if rem in factors:
				factors[rem] += 1
			else:
				factors[rem] = 1
			rem = 1
	return factors

def euler_phi(n,epdict={1:1}):
	if n in epdict:
		return epdict[n]
	factors = prime_factorize(n).items()
	p = factors[0][0]
	power = factors[0][1]
	if len(factors) == 1:
		epdict[n] = p**(power)-p**(power-1)
		return epdict[n]
	epdict[n] = euler_phi(p**power)*euler_phi(n/p**power)
	return epdict[n]

def fast_mod_pow(base,exp,mod,acc=1):
	while exp != 0:
		if exp % 2 == 0:
			base = base*base%mod
			exp /=2
		else:
			#return fast_mod_pow(base*base%mod,exp/2,mod,acc)
			exp-=1
			acc= acc*base %mod
#		return fast_mod_pow(base,exp-1,mod,acc*base%mod)
	return acc%mod

#a,b have no common factors
#so b %a cannot be zero. and b^-1 = b**(a-1)
def predecessor(a,b,maxsize):
	n = ((a*maxsize-1)/b)
	binv = euler_phi(a)-1
	if (b*n +1)%a != 0:
		#(b*(n-k)) mod a= -1 mod a
		#-b*k=-1-b*n
		#-k = (-1-b*n)*b^-1
		bk = -1-b*n
		k = (-(bk*(fast_mod_pow(b,binv,a))))%a
		n -= k
	m = (1+n*b)/a
	return n,m

def predecessor_count(a_start,b_start,a_end,b_end,maxsize):
	a = a_start
	b = b_start
	count = -1 #first doesn't count
	while not ((a == a_end) and (b == b_end)):
		count +=1
		n = ((a*maxsize-1)/b)
		binv = euler_phi(a)-1
		if (b*n +1)%a != 0:
			bk=-1-b*n
			k = (-(bk*(fast_mod_pow(b,binv,a))))%a
			n-=k
		m=(1+n*b)/a
		a=n
		b=m
	return count

if __name__ == "__main__":
	print predecessor(3,7,10**6)
