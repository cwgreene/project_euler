import primes
import math

def squarefree(max):
	primes.init(int(math.sqrt(max))+1)
	squareburdened = 0
	for p in primes.primes_list:
		p = int(p)
		already = squareburdened/p**2
		thisnum = max/p**2
		squareburdened += int(thisnum-already)
	return max - squareburdened

def check_list(alist):
	def is_squarefree(n):
		for p in primes.primes_list:
			if n%p**2==0:
				return False
		return True
	return filter(is_squarefree,alist)
num =  524
result =squarefree(num)
check= len(check_list(range(1,num+1)))
print result,check
