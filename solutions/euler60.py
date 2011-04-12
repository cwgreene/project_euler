#status: works. very slow. :( 1m40 seconds
#50 seconds if we make sure all primes get preloaded

import primes as pr
import itertools as it
import networkx
import cProfile

def is_concat(p1,p2,misconcat={}):
	if (p1,p2) in misconcat:
		return misconcat[(p1,p2)]
	misconcat[(p1,p2)]=False
	if (pr.is_prime(pr.concat_nums(p1,p2)) 
		and pr.is_prime(pr.concat_nums(p2,p1))):
		misconcat[(p1,p2)] = True
		misconcat[(p2,p1)] = True
	return misconcat[(p1,p2)]

#currently, we don't do this very nicely
#we look at all the outgoing nodes,
#and considering all subsets of length n of them
#if that n-set all share n common pairs, then it's good.
#we search the graph so that we will get the lowest numbers
#possible? not necessarily, but we will find the subgraphs.
#so it's a bug, but not currently a problem because currently
#the search is too big.
#need to figure out what the overlap is to reduce it.
def find_complete_subgraph(graph,n):
	sol = None
	print "find_complete_subgraph"
	for p in  sorted(graph.keys()):
		if len(graph[p]) >= n:
			sol = set(graph[p])	
			for combination in it.combinations(sorted(graph[p]),n):
				sets = [graph[k] for k in combination]
				sol2 = sol.intersection(*sets)
				if len(sol2) >= n:
					return sol2

def solutions(n,k):
	sub_prime = pr.primes_list[:n]
	#this might take about 20 seconds
	#
	#print "sub_prime",sub_prime,len(sub_prime)
	num_primes = len(sub_prime)
	concatenable_pairs = {}
	for p in pr.primes_list[:n]:
		concatenable_pairs[p] = [p]
	pairs = it.product(sub_prime,sub_prime)
	print "iterating"
	G = networkx.Graph()
	for p1,p2 in pairs:
		if p1 < p2:
			if is_concat(p1,p2):
				G.add_edge(p1,p2) #if we checked
						  #now, we'd probably
						  #be fine.
	print "clique finding"
	cliques = networkx.find_cliques(G)
	poss = filter(lambda x: len(x) == k,cliques)
	if poss != []:
		poss = min(poss,key=lambda x:sum(x))
	return poss
	#return find_complete_subgraph(concatenable_pairs,k)

def main():
	sol = []
	prime_length = 10**8
	pr.init(prime_length)
	primes = 1
	while sol == []:
		if primes > prime_length:
			pr.init(primes)
		sol = solutions(1200,5)
	print sol
	print "answer:",sum(sol)

if __name__ == '__main__':
	main()
