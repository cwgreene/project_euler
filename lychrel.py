def reverse_number(n):
	reversed_n = int("".join([a for a in reversed(str(n))]))
	return reversed_n

mporder = {}
switch = False
def porder(n,i):
	if n in mporder:
		return mporder[n]
	if i > 50:
		return 50
	reversed_n = reverse_number(n)
	sum = reversed_n+n
	if reverse_number(sum) == sum:
		mporder[n]=1
	else:
		depth = porder(sum,i+1)+1
		mporder[n] = depth
	return mporder[n]

def get_porder(n):
	return porder(n,1)	
