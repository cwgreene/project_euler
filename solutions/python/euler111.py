import itertools as it
import primes

def enumerate_digits(n_fixed,digit,k):
	result = [0]*k
	#pick empty slots
	final_result = []
	if n_fixed == k:
		num = int(str(digit)*k)
		if primes.is_prime(num):
			return [num]
		return []
	for slots in it.combinations(range(k),n_fixed):
		for num in xrange(10**(k-n_fixed)):
			i = 0
			astr = str(num)
			astr = '0'*(k-n_fixed-len(astr))+astr
			for spot in range(k):
				if spot in slots:
					result[spot] = str(digit)
				else:
					result[spot] = astr[i]
					i+=1
			num =int("".join(result))
			if len(str(num)) != len(result):
				continue
			if primes.is_prime(num):
				final_result.append(num)
	return final_result
def sum_fixed_n(n):
	marked = set()
	tsum = 0
	for i in range(n,1,-1):
		for d in range(10):
			if d not in marked:
				primes_res = enumerate_digits(i,d,n)
				if len(primes_res) != 0:
					print "digit",d,primes_res
					marked.add(d)
					tsum += sum(primes_res)
	print tsum
def main():
	primes.init(100)
	sum_fixed_n(10)
main()
