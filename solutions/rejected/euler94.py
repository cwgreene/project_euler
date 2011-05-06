import math

def angles(n):
	return math.acos((n+1.)/(2*n)),math.acos((n-1.)/(2*n))

def areas(n):
	areas = tuple()
	for theta in angles(n):
		areas += (n*math.sin(theta)*(n+1.)/2,)
	return areas

def sum_valid(areas,n,max):
	big,small = areas
	total = 0
	if int(big) == big and 3*n+1 < max:
		total += 3*n+1
	if int(small) == small and 3*n-1 < max:
		total += 3*n-1
	return total

total = 0
n=2
while 3*n-1 < 10**9:
	total+=sum_valid(areas(n),n,10**9)
	n+=1
	print n
print total
