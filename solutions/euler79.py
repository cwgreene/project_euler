def parse_file(filename)
	file = open(filename)
	lessthan = {}
	greaterthan = {}
	for line in file:
		nums = line.strip().split()
		for i,num in enumerate(nums):
			for less in nums[i+1:]:
				lessthan[num] =  less
			for greater in nums[:i]:
				greaterthan[num] = greater
	return lessthan,greaterthan

def subdict(adict,keyvalue):
	result = {}
	for k,v in adict:
		if k != keyvalue:
			adict[k]=
	return result

def satisfy_constraints(constraints):
	result = []
	lessthan,greaterthan = constraints
	keyslt = lessthan.keys()
	keysgt = greaterthan.keys()
	#if keyslt is empty, we're done
	if lens(keyslt) == 0:
		return []
	#take first key, and put it into result
	thisvalue = keyslt[0]
	result.append(thisvalue)

	lessthanext = {}
	for key in lessthan:
		if thisvalue in lessthan[key]:
			
	
