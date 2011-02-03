#below seems to be a wrong implementation. This needs to be corrected
#... as soon as I can figure out how I did it.

import primes as p

def tryit(special,memo={}):
	print special
	if special in memo:
		return memo[special]
	memo[special]= None
	result = None
	for prime in p.primes_list:
		count = 0
		if prime in special:
			continue
		for s in special:
			if p.is_prime(p.concat_nums(prime,s)):
				if p.is_prime(p.concat_nums(s,prime)):
					count +=1
		if count == len(special):
			result = special+(prime,)
			break
	if result == None:
		for i in range(len(special)):
			for prime in p.primes_list[1:]:
				if prime not in special:
					result = tryit(special[:i]+(prime,)
							+special[i+1:])
					if result:
						print result
						break
			if result:
				break
	memo[special] = result
	return memo[special]

if __name__=="__main__":
	p.init(1*10**4)
	print sum(tryit((3,7,109,673)))
