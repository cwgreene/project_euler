import primes
from collections import OrderedDict

#two problems, enumerating prime products

def enumerate_prime_products(primelist,max):
	pq = PriorityQueue()
	first = ((2,),2)
	pq.put(first)
	curval = first
	nextprimeindex = 1
	while curval < max:
		#get next lowest
		factors, curval = pq.get()
		nextprime = primelist[nextprimeindex]
		if curval > primelist[nextprimeindex]:
			pq.put((factors,curval))
			pq.put((
		for i,factor in enumerate(factors):
			result = (factor[:i]+(factor[i+1],)+factor[:-1]),factor*curval
			pq.put(result)
		pq.put(



def main():
	primes.init(10**5)
	place = 1
	curval = 1
	while place < 10000:
		#for each prime brought in
		#find out how far we get pushed forward
main()
