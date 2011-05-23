#this is a quick and dirty solution
#A better way, so that the fibonacci calc goes faster (as well as
#the str transform)
#is to just keep track of the last 10 digits. Once we find a candidate
#we use fast_fib to quickly recover the first 10 digits.


#this used to be a modulo k version
#but to do it that way, you need to do fast_fib
#and I got lazy.
def fibonacci_mod(prev1,prev2,k):
	return (prev1+prev2),prev1

#fast calc for fib
#def fast_fib(n):
	#fast fib is really simple
	#you say Hey! Fibonacci is just a matrix transformation 
	#of the prev1 and prev2 vector!
	#and exponentiating a vector can be done quickly, just
	#like regular fast exponentiation!
	#

		
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
