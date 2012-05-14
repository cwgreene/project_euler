from common_funcs import choose

def rects(n,m):
	total = 0
	for lengthx in range(1,n+1):
		for lengthy in range(1,m+1):
			total+=(n-lengthx+1)*(m-lengthy+1)
	return total

def rects_fast(n,m):
	return  (n**2-n*(n+1)/2+n)*(m**2-m*(m+1)/2+m)

#the following is a really bad way of solving this.
#we should instead find the upperbound for a single number
#and then proceed to find the nearest for each one, then proceed
#to take the nearest (which can be found using binary search since 
#the function is monotonically increasing)

#the number 2000 comes from the fact that  rects(2000,1) is
#greater than 2 million. From the monotonic property, if know that
#the second argument will only increase this value, so we're
#somewhere else.
min = 2*10**6
minval = (0,0)
for n in xrange(1,2000+1):
	for m in xrange(1,2000+1):
		curval = abs(rects_fast(n,m)-2*10**6)
		if curval < min:
			min = curval
			minval = n,m
print minval[0]*minval[1]
