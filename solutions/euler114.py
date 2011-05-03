def count_blocks(minsize,maxsize,remaining,mcount={}):
	if (minsize,maxsize,remaining) in mcount:
		return mcount[(minsize,maxsize,remaining)]
	total = 0
	#pick a size
	for size in range(minsize,maxsize+1):
		#figure out where to plop it down
		for start in range(remaining-size+1):
			total += 1 + count_blocks(minsize,maxsize,
						remaining-(size+start+1))
	mcount[(minsize,maxsize,remaining)] = total
	return total
print 1+count_blocks(3,50,50)

