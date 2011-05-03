#we add the additional constraint
#that two blocks may not be adjacent
#so that we don't multiply count single
#long blocks with side by side blocks

#the additional proposed constraint might
#actually make this much harder. I think
#we can actually ignore it given the
#way the recursion works and since
#we aren't attempting to reconstruct the moves
def block_counts(n,minsize,mbc={}):
	if (n,minsize) in mbc:
			return mbc[(n,minsize)]
	if n <= 0:
		return 0
	if n < minsize:
		return 1
	total = 2*block_counts(n-minsize,minsize)
	for x in range(1,minsize):
		total += block_counts(n-x-minsize,minsize)
	mbc[(n,minsize)] = total
	return total

for x in range(1,7+1):
	print x,block_counts(x,3)
			
