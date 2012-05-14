#when -(1/4)-n/2+3n^2/4 is square
#then n is a valid n,n,n+1 near equilateral
import math

def integer_roots(a,b,c):
	result = ()
	discriminant = b**2-4*a*c
	if discriminant < 0:
		return result
	if int(math.sqrt(discriminant))**2 != discriminant:
		return ()
	rootdisc = math.sqrt(discriminant)
	top_plus = -b+rootdisc
	top_minus = -b-rootdisc
	if top_plus % (2*a) == 0 and top_plus/(2*a) >= 0:
		result = top_plus/(2*a)
	if top_minus % (2*a) == 0 and top_minus/(2*a) >= 0:
		result = top_mins/(2*a)
	return result

def find_all_by_k(max):
	#maxroot = int(math.sqrt(max))
	result = []
	for k in xrange(2,max+1,1):
		for n in ([(integer_roots(.75,-.5,-k**2-.25),"+")]+
				[(integer_roots(.75,.5,-k**2-.25),"-")]):
			if n[0] != ():
				print k,n,k%3,n[0]%4
				result.append((k,n))
	return result

def is_square(n):
	root = int(math.sqrt(n))
	return root*root==n

def find_all_by_n(max):
	result = []
	for n in xrange(5,max,4):
		nmin = n*(2+3*n)-1
		nplus = (3*n-2)*n-1
		if is_square(nmin/4):
			print n
			result.append((n,n-1))
		if is_square(nplus/4):
			print n
			result.append((n,n+1))
	return result


res = find_all_by_n((10**9+1)/3)
print res
print "sum:",sum([2*x[0]+x[1] for x in res])
