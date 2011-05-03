import primes

from Queue import PriorityQueue

from common_funcs import choose_degen,degen_list,degen_product

def combinations_distinct(alist):
	total = 0
	for x in range(1,len(alist)+1):
		total += choose_degen(alist,x)*2**(x-1)
	return total+1


def findmax(n):
	for x in range(1,n):
		dlist =  degen_list(range(x))
		if combinations_distinct(dlist) > n:
			return x

def viable(curprimes,index,max,n):
	prime,count = curprimes[index]
	cur_count = 0
	for x in curprimes[:index]:
		cur_count+=x[1]
	cur_count += count+1
	nextprimes = (curprimes[:index]+((prime,count+1),)+
			tuple(degen_list(range(max-cur_count))))
	if combinations_distinct(nextprimes) < n:
		return False
	return True

def enumerate_min(n):
	pl = primes.primes_list

	#graph
	startnode =  (2,((2,1),))
	"""(2,((2,1),(3,1),(5,1),
			(7,1),(11,1),(13,1),
			(17,1),(19,1),(23,1),
			(29,1),(31,1),(37,1)))"""
	nodes = set(startnode)
	nextnodes = PriorityQueue()
	nextnodes.put(startnode)
	cur_node = nextnodes.get()
	cur_comb = combinations_distinct(cur_node[1])
	
	max_found = 0
	#print max,raw_input()
	while cur_comb < n:
		value,curprimes = cur_node
		#nextnodes are added
		#we increment an existing primes, and we add an existing
		#add 1 to each existing prime
		prev = curprimes[0][1]+1
		for i,p in enumerate(curprimes):
			prime,count = p
			if count+1 > prev:
				break
			prev = count+1
			#check if this way can even theoretically get
			#us to where we want
			newprimes = (curprimes[:i]+
					((prime,count+1),)+
					curprimes[i+1:])
			newnode = degen_product(newprimes),newprimes
			if newnode not in nodes:
				nodes.add(newnode)
				nextnodes.put(newnode)
		#add new prime
		newprimes = curprimes+((int(pl[(len(curprimes))]),1),)
		newvalue = degen_product(newprimes)
		newnode = newvalue,newprimes
		if newnode not in nodes:
			nodes.add(newnode)
			nextnodes.put(newnode)
		cur_node = nextnodes.get()
		cur_comb = combinations_distinct(cur_node[1])
		value,curprimes = cur_node
		if cur_comb> max_found:
			print (value,cur_comb,curprimes)
			max_found = cur_comb
	print cur_node,combinations_distinct(cur_node[1])

def main():
	primes.init(1000)
	print "hi"
	enumerate_min(4*10**6)

main()
