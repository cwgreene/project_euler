"""
#cheap ass solution. would take 2 hours
count = 0
for x in xrange(1,10**6):
	fail = False
	strx = str(x)
	if strx[-1] == "0":
		continue
	res = str(x+int((str(x))[::-1]))
	for digit in res:
		if int(digit) %2 == 0:
			fail = True
			break
	if not fail:
		count +=1
print count
"""

#odd_conjugates computes the number 
#that can 
def odd_pairs_no_carry(digits):
	if digits == 0:
		return 0
	total = 0
	for x in range(0,10+1):
		
def odd_pairs_carry(digits):
	if digits == 0:
		return 0
	
