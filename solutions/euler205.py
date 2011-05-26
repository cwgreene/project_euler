def number_ways(n,k,max_side,mnum={}):
	if (n,k,max_side) in mnum:
		return mnum[(n,k,max_side)]
	if n == 0 and k == 0:
		return 1
	if k <= 0 or n <= 0:
		return 0
	total = 0
	for i in range(1,max_side+1):
		total += number_ways(n-i,k-1,max_side)
	mnum[(n,k,max_side)] = total
	return total

def main():
	ways_pete_beats_colin = 0
	total_outcomes = (6**6)*(4**9)
	for x in range(9,36+1):
		peter_ways = number_ways(x,9,4)
		colin_ways = 0
		for y in range(6,x):
			colin_ways += number_ways(y,6,6)
		total_ways = colin_ways*peter_ways
		ways_pete_beats_colin+= total_ways
	print round(ways_pete_beats_colin*1./total_outcomes,7)

print number_ways(6,6,6)
main()
