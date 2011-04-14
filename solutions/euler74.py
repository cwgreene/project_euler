def fac(n,mfac={0:1}):
	if n in mfac:
		return mfac[n]
	res = n*fac(n-1)
	mfac[n] = res
	return res

def sumfac(n):
	return sum([fac(int(a)) for a in str(n)])

def chain(n,f,mchain={}):
	if n in mchain:
		return mchain[n]
	mchain[n] = 0
	next = f(n)
	mchain[n] = chain(next,f,mchain)+1
	return mchain[n]
count =0
for x in range(1,10**6):
	if chain(x,sumfac)==60:
		count += 1
print count
