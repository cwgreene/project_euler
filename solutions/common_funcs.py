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
