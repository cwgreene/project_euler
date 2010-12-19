mcombo = {}
def combo(n,m,max=200):
	if (n,m,max) in mcombo:
		return mcombo[(n,m,max)]
	if n <= 0:
		return 0
	result = 0
	denominations = [1,2,5,10,20,50,100,200]
	if m == 1:
		if n in denominations:
			if n <= max:
				result = 1
			else:
				result = 0
		else:
			return 0
	else:
		sum = 0
		for x in denominations:
			if x <= max:
				sum += combo(n-x,m-1,x)
		result = sum
	mcombo[(n,m,max)] = result
	return result
		
#for x in range(1,200+1):
for value in range(1,200+1):
	for count in range(1,200+1):
		combo(value,count)

sum = 0
for x in xrange(1,200+1):
	sum+=combo(200,x)
print sum
