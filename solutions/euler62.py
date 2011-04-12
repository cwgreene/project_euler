digit_primes = [2,3,5,7,11,13,17,23,29,31]
#euler 62

#improvement can be done in main
#so that we don't just pick a magic number
#simplest way I can think of is just wait until
#cube digits increase. We might want another dict
#that keeps track of people who have gotten a 5.
def digit_hash(num):
	numstr = str(num)
	acc = 1
	for x in numstr:
		acc *= digit_primes[int(x)]
	return acc

def main():
	count = {}
	biggest = 10**5 #magic
	for cube,hash in [(x**3,digit_hash(x**3)) for x in range(biggest)]:
		if hash not in count:
			count[hash] = [cube,1]
		else:
			count[hash][1] += 1
	min = biggest**3
	for hash in count:
		if count[hash][1] == 5 and min > count[hash][0]:
			min = count[hash][0]
	print min

if __name__=="__main__":
	main()
