import primes

def main():
	primes.init(10**6)
	sums = [0]*(10**6+1)
	for x in range(1,10**6):
		primes.factor(x)
		print x
	print x

if __name__=="__main__":
	main()
