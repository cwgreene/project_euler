#brute force it, only 10! possibilities
import itertools as it

for x in it.permutations(range(1,10+1)):
	extremals = [x[i] for i in [0,3,4,7,9]]
	if x[0] == min(extremals):
		sum1 = x[0]+x[1]+x[2]
		sum2 = x[3]+x[2]+x[5]
		sum3 = x[4]+x[5]+x[6]
		sum4 = x[7]+x[6]+x[8]
		sum5 = x[9]+x[8]+x[1]
		if sum1==sum2==sum3==sum4==sum5:
			print 	"".join(map(str,(x[0],x[1],x[2],
				x[3],x[2],x[5],
				x[4],x[5],x[6],
				x[7],x[6],x[8],
				x[9],x[8],x[1])))
			
