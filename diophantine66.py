import math

def minimal(D):
	x = math.ceil(math.sqrt(D))
	y = 1
	while x**2 - D*y**2 != 1:
		
