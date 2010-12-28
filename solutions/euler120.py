#Problem 120
#
#Expanding the term (a-1)^n
#yields a polynomial of the form
#a^n - n*a^(n-1) + c(n,2)a^(n-2)....+n*(-1)^(n-1)*a+(-1)^(n)
#
#Only the last two terms are not divisible by a^2.
#
#For (a+1), similarly, the result is
#a*n +1
#
#if n is even, then n-1 is odd, so the result is 2 (the a's cancel)
#if n is odd, then n-1 is even, so the result is 2*a*n mod a^2 
# (the 1's cancel)
#
#so to maximize this we will always have a^2-a=(a-1)*a when a is odd
#but when a is even, then 2*n will divide the number, so we can't nestle
#directly up to it

def r_max(a):
	if a% 2 == 0:
		return (a-2)*a
	return (a-1)*a

if __name__=="__main__":
	print sum(map(r_max,range(3,1000+1)))
