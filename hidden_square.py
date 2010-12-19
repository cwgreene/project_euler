"""problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each _ is a single digit."""

def verify(x):
	for val,exp in zip([0,9,8,7,6,5,4,3,2,1],range(10)):
		digit = (x % 10**(2*exp+1 ))/(10**(2*exp))
		if digit != val:
			return False
	return True

#this is an absoultely terrible way to solve it.
#Not how we came up with the ranges
#we said "Hey! it has to be somewhere between
#the square root of 1020304050607080900
#and the square root of 1929394959697989990
#that's all well and good, but what we should do
#is once the second digit is no longer 2
#we should recalculate where to start checking next
#we could even recursively do this all the way down.
#in fact, that might just do it exactly with pencil and paper
#...
#wait a second... isn't this just replacing everything?
def bad_method():
	for x in xrange(1010100960, 1389026624,10):
		if verify(x*x):
			print "solution:",x
			break
		if x % 90000 == 0:
			print x,x*x

def digit(x,n):
	digit = (x % 10**(n+1))/(10**(n))
	return digit

def min_max(first_digit):
	z = ("1"+str(first_digit)+"2_3_4_5_6_7_8_9_0")
	min = int(math.sqrt(int(z.replace("_","0"))))
	max = int(math.sqrt(int(z.replace("_","9"))))+1
	min = (min/10)*10 #ensure divisibility
	return min,max

def hopefully_better():
	for first_digit in range(10):
		min,max = min_max(first_digit)
		for x in xrange(min,max,10):
			if verify(x*x):
				print "solution",x
				break	
			if x %10000 == 0:
				print x,x*x
