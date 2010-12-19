from numpy.random import *

def random_pi(n):
	xs = 2*rand(n)-1
	ys = 2*rand(n)-1
	print xs*xs+ys*ys
	num = (xs*xs +ys*ys) < 1
	return sum(num)*1.0/n
