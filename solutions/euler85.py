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
#to take the nearest.
result=[(abs(rects_fast(n,m)-2*10**6),n,m) for n in range(1,1000) 
			for m in range(1,1000)]
result.sort()
print result[0]
print result[0][1]*result[0][2]
