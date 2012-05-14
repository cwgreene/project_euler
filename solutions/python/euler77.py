import primes
import itertools as it

print "Starting Euler77"

maxval,max = 0,0

def stagger_iterate(alist, blist, notequal, equal,cmp=cmp): 
	#setup 
	indices = [0,0] 
	def inc_x(which,func,x,y): 
		for i in which: 
			indices[i] += 1 
		func(x,y) 
	cmpfunc = {-1: lambda x,y:inc_x([0],lambda x,y: notequal(x),x,y), 
		    0: lambda x,y:inc_x([0,1],equal,x,y), 
		    1: lambda x,y:inc_x([1],lambda x,y: notequal(y),x,y)} 

	#iteration here 
	while indices[0] < len(alist): 
		if indices[1] < len(blist): 
			(cmpfunc[cmp(alist[indices[0]],
				blist[indices[1]])]
			(alist[indices[0]],blist[indices[1]]))
		else: 
			cmpfunc[-1](alist[indices[0]],0) 
	while indices[1] < len(blist): 
		cmpfunc[1](0,blist[indices[1]])


#potentially useful control structure
#stagger-iterate x in alist,blist
#	do stuff with x (which is the next greatest between alist and blist)
#if-equal x,y
#	do stuff with x and y
def merge_decomp(alist,blist):
	reslist = []
	def merge_append(x,y):
		reslist.append((x[0],x[1]+y[1]))
	stagger_iterate(alist,blist,
			notequal=lambda x: reslist.append(x),
			equal=merge_append,
			cmp = lambda x,y:cmp(x[0],y[0]))
	return reslist

class Decomposition(object):
	def __init__(self,num):
		self.num = num
		self.decomp = ((num,1),)
	def __add__(self,other):
		res = Decomposition(self.num+other.num)
		
		#merge
		reslist = []
		def merge_append(x,y):
			reslist.append((x[0],x[1]+y[1]))
		stagger_iterate(self.decomp,other.decomp,
			notequal=lambda x: reslist.append(x),
			equal=merge_append,
			cmp = lambda x,y:cmp(x[0],y[0]))
		res.decomp = tuple(reslist)
		return res
	def __repr__(self):
		res = ""
		for x in self.decomp:
			res += "+"
			res += (str(x[0])+"+")*x[1]
			res = res[:-1]
		res = res[1:]
		return res
	def __eq__(self,other):
		if self.num != other.num:
			return False
		return self.decomp == other.decomp
	def __hash__(self):
		return hash((self.num,self.decomp))

#use memo trick
total_collisions = 0
def decompose_into_count(number,subset, decomps = {0:set([])}):
	global total_collisions
	dic = decompose_into_count
	if number in decomps:
		return decomps[number]
	decomps[number]=set([])
	for p in subset:
		if p > number:
			break
		if p == number:
			decomps[number].add(Decomposition(p))
		for x in dic(number-p,subset):
			for y in dic(p,subset):
				z = x+y
				if z in decomps[number]:
					total_collisions +=1
				decomps[number].add(z)
	return decomps[number]

for n in it.count():
	count =  len(decompose_into_count(n,primes.primes_list))
	if max < count:
		max = count
		maxval = n
		print maxval,max
		print total_collisions
	if max > 5000:
		break
print maxval
