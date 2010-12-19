import euler
import time

chains = {89:89,1:1}
sum_time = 0

def next_chain(x):
	square_digits = [d*d for d in euler.digits(x)]
	return sum(square_digits)

def next_chain_fast(x): #not that much faster
	global sum_time
	start = time.time()
	sum =0
	prev_power = 1
	power = 10
	while x/(prev_power) != 0:
		product=(x % power)/(prev_power)
		sum += product*product
		power *=10
		prev_power *= 10
	sum_time += time.time()-start
	return sum

def run_chain(n):
	cur = n
	if n in chains:
		return chains[n]
	if n > 1000:
		return chains[next_chain(n)]
	chains[n] = 0 #terminate backtrack, is never 0
	while cur != 1 and cur != 89: #go until 89 or 1
		prev = cur	 #remember the current
		cur = next_chain(prev) #get the new cur
		chains[cur] = prev	#set the current to point back
	final = cur #89 or 1
	while cur != n: #backtrack
		prev = chains[cur] #previous is the current's value
		chains[cur] = final #set the current to correct value
		cur = prev
	chains[n] = final
	return final

def percent(n,m):
	count =0
	for x in range(1,1000):
		if run_chain(x) == m:
			count +=1
	for x in xrange(1000,n): #DO NOT USE ZERO
		next = next_chain(x)
		if chains[next] == m:
			count +=1
	return count
