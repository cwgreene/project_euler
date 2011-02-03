#we are solving the equation
#n/m * (n-1)/(m-1) = 1/2
#yielding n**2-n = m*(m-1)/2
#
#A brute force solution (probably should not be attempted)
#would require us to determine quickly if a given number
#is of the form n**2-n. One way is to solve for n directly
#and check if it's an integer. This may not be too bad
#since we get to deal with squares, so 10**12 is two millions*
#
#The n**2-n-m*(m-1)/2 = 0
#will have an integer solution if 
#-b+/-sqrt(b^2-4*a*c)/2*a is an integer
#which means the numerator must an integer divisble by two
#which means that
#sqrt(1+4*(m*(m-1))/2) is an integer (and odd, since b is 1)
#which means 1+2*(m*(m-1)) is an odd square. It's automatically
#odd, due to the one, so we are left with just the square bit.

#*oops! The above brute force estimates was based on bad assumptions, namely
#that 10**12 is the total number of _possibilities_. They want
#10**12 to be the total number of _disks_. Oops.

#so we are interested in k**2=1+2*(m*(m-1))=1+2*m^2-m
#(1-k^2)+2*m^2-m
#1-4*(1-k^2)*(2) = 8*k^2-7 must be an square number

#8*k^2-7=z^2
#-4*(8)*(z^2+7)

import itertools as it
import math

def is_factorable(num):
	#a_p= (-1+math.sqrt(1-4*num))/2
	#a_m= (-1+math.sqrt(1-4*num))/2
	discrim= math.sqrt(1+(2*num))
	idiscrim = int(discrim)
	if idiscrim**2 == 1+2*num:
		return True
	return False

def brute_force(m_start=10**6+1):
	for m in it.count(m_start):
		if is_factorable(m*(m-1)):
			return (-1+math.sqrt(1+2*(m*(m-1))))/2

def brute_count():
	count = 0
	for m in range(1000000):
		if is_factorable(m*(m-1)):
			count +=1
			print m
	return count


def main():
	print brute_count()

if __name__=="__main__":
	main()
