#nospace version
def count_blocks(minsize,maxsize,remaining,mcount={}):
	if (minsize,maxsize,remaining) in mcount:
		return mcount[(minsize,maxsize,remaining)]
	total = 0
	#pick a size
	for size in range(minsize,maxsize+1):
		#figure out where to plop it down
		for start in range(remaining-size+1):
			total += 1 + count_blocks(minsize,maxsize,
						remaining-(size+start),
						mcount)
	mcount[(minsize,maxsize,remaining)] = total
	return total

total = 0 #empty
for size in [2,3,4]:
	total+=count_blocks(size,size,50)
print total
