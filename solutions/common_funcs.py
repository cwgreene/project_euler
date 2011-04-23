def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

def digit_hash(num,
		digit_primes = [2,3,5,7,11,13,17,23,29,31]):
	try:
		numstr = str(num)
		acc = 1
		for x in numstr:
			acc *= digit_primes[int(x)]
		return acc
	except:
		print "error",num,str(num)
		raise

def binary_search(alist,val,hi,lo,sign=1):
	mid = (hi+lo)/2
	if alist[mid] == val:
		return mid
	if hi <= lo:
		return mid
	if alist[mid]*sign < val*sign:
		return binary_search(alist,val,hi,mid+1)
	if alist[mid]*sign > val*sign:
		return binary_search(alist,val,mid-1,lo)

def fac(n):
	prod = 1
	for x in range(1,n+1):
		prod*= x
	return prod

def choose(n,k):
	return fac(n)/(fac(k)*fac(n-k))

def partitions_k(n,k,mpk={}):
	if (n,k) in mpk:
		return mpk[(n,k)]
	if k > n:
		mpk[(n,k)] = 0
		return 0
	if k== n:
		mpk[(n,k)] = 1
		return 1
	result = partitions_k(n,k+1)+partitions_k(n-k,k)
	mpk[(n,k)] = result
	return result

def partitions(n):
	total = 1
	#calculate downards to prevent recursive issues
	for x in range(n):
			partitions_k(n,n-x)
	for i in range(1,n/2+1):
		total += partitions_k(n-i,i)
	return total
