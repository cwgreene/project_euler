def is_pandigital(x):
	x = map(int,list(str(x)))
	if len(x) == 9:
		if set(x) == set([1,2,3,4,5,6,7,8,9]):
			return True
	return False

results = []
for x in xrange(10,100):
	for y in range(100,1000):
		if is_pandigital(str(x)+str(y)+str(x*y)):
			results.append((x,y,x*y))
			print x,y,x*y
for x in xrange(1,10):
	for y in range(1000,10000):
		if is_pandigital(str(x)+str(y)+str(x*y)):
			results.append((x,y,x*y))
			print x,y,x*y
print sum(set(map(lambda z:z[2],results)))
