#this is a quick and dirty solution
#implementing the fast


#this used to be a modulo k version
#but to do it that way, you need to do fast_fib
#and I got lazy.
def fibonacci_mod(prev1,prev2,k):
	return (prev1+prev2),prev1

#fast calc for fib
#def fast_fib(n):
	
z=0
prev1=0
prev2=1
count =0
for x in xrange(10**6):
	prev1,prev2= fibonacci_mod(prev1,prev2,10**9)
	digits = set(str(prev1 % 10**9))
	if '0' not in digits and len(digits)==9:
		first = set(str(prev1)[0:9])
		print x,first
		if '0' not in first and len(first) == 9:
			break
		#x = fast_fib(x+1)
print x+1
