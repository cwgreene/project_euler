import primes

def is_prime_divider(p):
	if 10 % p == 1: #could also say: not 3
		return False
	
	groupsize = p-1

	max2 = 0
	max5 = 0

	while groupsize % 2**(max2+1) == 0:
		max2 += 1
	while groupsize % 5**(max5+1) == 0:
		max5 += 1
	for pow2 in range(0,max2+2):
		for pow5 in range(0,max5+2):
			power = (2**pow2)*(5**pow5)
			if pow(10,power,p) == 1:
				return True
	return False

def find_all(max):
	result = []
	primes.init(max)
	for p in primes.primes_list:
		divides = is_prime_divider(int(p))
		if divides:
			result.append(p)
	return result

results = find_all(10**5)
print results
print sum(primes.primes_list)-sum(results)
