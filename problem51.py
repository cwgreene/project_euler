import goldbach
import itertools as it

primes = set(goldbach.primes)
results = set()

def numprimes(alist):
	return filter(lambda x: x in primes,alist)

def replace(numstr):
	for x in range(1,len(numstr)):
		for select in it.combinations(range(len(numstr)),x):
			numlist = list(numstr)
			all_nums = []
			for n in range(10):
				for i in select:
					if(i >= x or n != 0):
						numlist[i] = str(n)
				if(i >= x or n != 0):
					all_nums.append(int("".join(numlist)))
			all_nums = numprimes(all_nums)
			if len(all_nums) == 8:
				print all_nums
				return numlist
	return None
	
count = 10
print goldbach.primes[-1]
for x in goldbach.primes:
	if x > count:
		print x
		count *= 1.1
	if(replace(str(x))):
		print x
		break
