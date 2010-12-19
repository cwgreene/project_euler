#problem 66
import itertools as it
import math

def square_div(D):
	#look at squares divisible by D. See if (square+1)/D is also square
	for i in it.count(1):
		yield i**2

def find_x(D):
	for y_sq in square_div(D):
		x_sq = D*y_sq+1
		if int(math.sqrt(x_sq))**2 == x_sq:
			return math.sqrt(x_sq),math.sqrt(y_sq)
	return 0


def enumerate(the_range):
	xlist = []
	for D in range(1,the_range+1):
		if math.sqrt(D) != int(math.sqrt(D)):
			xlist.append((find_x(D),D))
			print D
	print xlist
	return xlist
