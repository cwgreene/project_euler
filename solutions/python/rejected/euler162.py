from common_funcs import choose

#DEGENERACY!!!!
#crud
#to fix, count all using _exactly_ k 0's
#the issue is this
#when we pick a slot, and enforce it to be A (or 1 or zero)
#Nothing stops us from having this counted possibly before
def calculate_hex(max):
	total = 0L
	#handle assuming lead is not zero
	for numdigits in range(3,max+1):
		#leading 1,choose 2 others, remember perms
		total += (choose(numdigits-1,2)*2)*(16**(numdigits-3))
		#leading A
		total += (choose(numdigits-1,2)*2)*(16**(numdigits-3))
		#leading other choose 3
		if numdigits >= 4:
			total += 13*((choose(numdigits-1,3)*6)*
				(16**(numdigits-4)))

	print total
	print hex(total)
	print (hex(total)[2:][:-1].upper())

calculate_hex(4)
