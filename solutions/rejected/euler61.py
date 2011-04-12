#status: unsolved
import math

def squares(n,m):
	squareset= set()
	for k in range(int(math.sqrt(n)),int(math.sqrt(m))+1):
		squareset.add(k*k)
	return squareset

def are_any_roots_naturals(poly):
	zeroes = roots(poly)
	for x in zeroes:
		if x>=1 and x == int(x):
			return True
	return False

def is_triangular(n):
	#k*(k+1)/2 = n=>2*n=k*k+k
	#k*(k+1)/2 = m
	return are_any_roots_naturals([1,-1,-2*n])

def is_pentagonal(n):
	#k*(3*k-1)/2 = n => 
	#2*n=k*(3*k-1)=>2*n=3*k^2-k
	return are_any_roots_naturals([3,-1,-2*n])

def is_hexagonal(n):
	#n = k*(2*k-1) => 0 = 2*k^2-1,n
	return are_any_roots_naturals([2,-1,-n])

def is_heptagonal(n):
	return are_any_roots_naturals([5,-3,-2*n])

def is_octagonal(n):
	return are_any_roots_naturals([3,-2,-n])

def roots(poly):
	if len(poly) != 3:
		raise("Only second orders work for now")
	#quadratic formula
	#root = (-b+/-sqrt(b^2-4*ac))/2
	(a,b,c) = poly
	root_p = (-b+math.sqrt(b**2-4*a*c))/(2.*a)
	root_m = (-b-math.sqrt(b**2-4*a*c))/(2.*a)
	return root_p,root_m
