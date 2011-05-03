def count_blocks(minsize,maxsize,remaining,mcount={}):
	if (minsize,maxsize,remaining) in mcount:
		return mcount[(minsize,maxsize,remaining)]
	total = 0
	#pick a size
	for size in range(minsize,maxsize+1):
		#figure out where to plop it down
		for start in range(remaining-size+1):
			total += 1 + count_blocks(minsize,maxsize,
						remaining-(size+start+1),
						mcount)
	mcount[(minsize,maxsize,remaining)] = total
	return total
x=50
total = count_blocks(50,x,x)
while total < 10**6:
	print total,x
	x+=1
	total = count_blocks(50,x,x)
print "Answer:",total,x

