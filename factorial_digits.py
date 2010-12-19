mfac = {}
def fac(n):
	if n in mfac:
		return mfac[n]	
	prod = 1
	for x in xrange(1,n+1):
		prod*=x
	mfac[n] = prod
	return prod
	
def sfac(n):
	return mfac[n]

def is_fac_digits(x):
	digits = map(int,list(str(x)))
	if sum(map(sfac,digits))==x:
		return True
	return False

def init_fac():
	for x in range(0,10):
		fac(x)
	return

