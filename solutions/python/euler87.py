import primes

def p(i):
	return primes.primes_list[i]

def prime_power_less(power,n,index):
	return p(index)**power <= n

def sum234(a,b,c):
	return p(a)**2+p(b)**3+p(c)**4

def number_of_ways(n,cheap_check=set()):
	total = 0
	fourth_prime = 0
	while prime_power_less(4,n,fourth_prime):
		sub_total3 = 0
		third_prime = 0
		n3 = n-p(fourth_prime)**4
		while prime_power_less(3,n3,third_prime):
			n2 = n3-p(third_prime)**3
			second_prime = 0
			sub_total2 = 0
			while prime_power_less(2,n2,second_prime):
				res = sum234(second_prime,third_prime,
						fourth_prime)
				"""print ((p(second_prime)**2
					+p(third_prime)**3
					+p(fourth_prime)**4),res,
					p(fourth_prime),p(third_prime),
					p(second_prime),n,n3,n2)"""
				cheap_check.add(res)
				sub_total2 += 1
				second_prime += 1
			sub_total3 += sub_total2
			third_prime += 1
		total += sub_total3
		fourth_prime += 1
	return len(cheap_check),total

def main():
	primes.init(50*10**6)
	print number_of_ways(50*10**6)
main()
