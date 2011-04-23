import math

#some increasing numbers are also decreasing numbers
#these are all numbers with the same digit

#number of bouncy numbers up to d digits
def non_bouncy(d):
	both = sum([increasing_decreasing(a) for a in range(1,d+1)])
	inc = sum([increasing(a) for a in range(1,d+1)])
	dec = sum([decreasing(a) for a in range(1,d+1)])
	return inc+dec-both

#these functions could be explicitly reduced
#into sum functions, which will make them run very fast
#but since it's already only summing on the digits, it's 
#already fast enough

def increasing_decreasing(d):
	return 9

def increasing_k(d,x,minc={}):
	if (d,x) in minc:
		return minc[(d,x)]
	if d == 0:
		return 1
	total = 0
	for a in range(x,9+1):
		total += increasing_k(d-1,a)
	minc[(d,x)] = total
	return total

def increasing(d):
	total = 0
	for x in range(1,9+1):
		total += increasing_k(d-1,x)
	return total

def decreasing_k(d,x,mdec={}):
	if (d,x) in mdec:
		return mdec[(d,x)]
	if d == 0:
		return 1
	total = 0
	for a in range(0,x+1):
		total += decreasing_k(d-1,a)
	mdec[(d,x)] = total
	return total

def decreasing(d):
	total = 0
	for x in range(1,9+1):
		total += decreasing_k(d-1,x)
	return total

print non_bouncy(100)
#def decreasing(d):

