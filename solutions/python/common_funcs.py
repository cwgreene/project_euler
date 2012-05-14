def fast_mod_pow(base,exp,mod,acc=1):
	while exp != 0:
		if exp % 2 == 0:
			base = base*base%mod
			exp /=2
		else:
			#return fast_mod_pow(base*base%mod,exp/2,mod,acc)
			exp-=1
			acc= acc*base %mod
#		return fast_mod_pow(base,exp-1,mod,acc*base%mod)
	return acc%mod
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
		prod *= x
	return prod

def choose(n,k):
	return fac(n)/(fac(k)*fac(n-k))

def degen_list(alist):
	indices = {}
	result = []
	cur_index = 0
	for key in alist:
		if key not in indices:
			indices[key] = cur_index
			cur_index += 1
			result.append((key,1))
		else:
			key, count = result[indices[key]]
			result[indices[key]] = (key,count+1)
	return result

def degen_product(dlist):
	p = 1
	for value,count in dlist:
		p *= value**count
	return p

def choose_degen(alist,k):
	if k > len(alist):
		return 0
	if k < 0:
		return 0
	if len(alist) == 0:
		return 1
	val,degen = alist[0]
	return (degen*choose_degen(alist[1:],k-1) +
			choose_degen(alist[1:],k))

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
		for y in range(n):
			partitions_k(x,n-y)
	for i in range(1,n/2+1):
		total += partitions_k(n-i,i)
	return total
