#master equatino
#
#  minmulthelp n^a*n^b= 1+minmult(n^a)+minmult(n^b)
#			- len(intersection(a,b))
#  minmult = min(minmulthelp)

minmult = {1:1}
minsets = {1:[set([1])]}

def find_minmult(n):
	if n in minmult:
		return minmult[n]
	minset = []
	min = 10**6
	for a in range(n/2,n):
		#b < a; n > a,b
		b = n-a
		for minimal_setb in minsets[b]:
			for minimal_seta in minsets[a]:
				result = minimal_seta.union(minimal_setb)
				result.add(n)
				tempmin = len(result)
				if tempmin < min:
					min = tempmin
					minset = [result]
				if tempmin == min:
					if result not in minset:
						minset.append(result)
	minmult[n] = min
	minsets[n] = minset
	return min

total = 0
for x in range(1,31+1):
	print x,find_minmult(x)-1,len(minsets[x])
	total +=len(minsets[x][0])-1
print minsets[31]
print total

