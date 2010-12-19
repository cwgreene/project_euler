import goldbach
import itertools as it
results =[]
print "Beginning"
n_all_primes = len(goldbach.primes)
max = 0
for id in xrange(n_all_primes):
	sum = 0
	if goldbach.primes[id]*max > 10**6:
		break
	for i,x in it.izip(it.count(),goldbach.primes[id:]):
		sum += x
		if sum > 10**6:
			break
		if goldbach.array[sum] != 0:
			results.append((i,id,sum))
			if i > max:
				max = i
				print i,sum,max
	if id %1000 == 0:
		print goldbach.primes[id],id,max,n_all_primes-id
print "done"
results = sorted(results)
print results[-1],goldbach.array[results[-1][2]]
