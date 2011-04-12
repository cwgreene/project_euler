import math

def find_x(D):
	y = 1
	test = square_root(1+D*y**2)
	while test*test != (1+D*y**2):
		y+=1
		test = square_root(1+D*y**2)
	return test

def square_root(x,hi=None,lo=0):
	if hi == None:
		hi = x
	cur = (hi+lo)/2
	if cur*cur == x:
		return cur
	if hi <= lo:
		return cur
	if cur*cur > x:
		return square_root(x,cur-1,lo)
	if cur*cur < x:
		return square_root(x,hi,cur+1)

def not_square(x):
	root = square_root(x)
	if root * root != x:
		return True
	return False

results = []
for D in filter(not_square,range(1000+1)):
	result = find_x(D)
	results.append(result)
	print D,result
print max(results)
	
