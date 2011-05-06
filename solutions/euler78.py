from common_funcs import partitions,binary_search

n = 1
count = partitions(1)
while count % 10**6 != 0:
	n+=1
	count=partitions(n)
	print n,count
