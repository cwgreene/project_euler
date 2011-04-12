def digit_hash(num,
		digit_primes = [2,3,5,7,11,13,17,23,29,31]):
	numstr = str(num)
	acc = 1
	for x in numstr:
		acc *= digit_primes[int(x)]
	return acc

