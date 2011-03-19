import itertools as it
import math

def rotshift(alist):
	return alist[1:]+alist[0:1]

def evaluate_continued_fraction(frac,n):
	a0,reps = frac
	if n == 0:
		return a0*1.
	acc = a0
	acc += 1/(reps[0]+evaluate_continued_fraction((0,rotshift(reps)),n-1))
	return acc

#the following, as one would expect does not work
#if num is not a float due to rounding
#So either tolerance must be introduced
#(which makes the dict approach mostly untenable)
#or the remainder most be made exact. This is doable
#for the purposes of roots
def construct_continued_fraction_wrong(num,acc=None,hist=None):
	if acc == None: acc = []
	if hist == None: hist = set()
	integer,frac = math.floor(num),num-math.floor(num)
	acc.append(integer)
	print integer,frac
	raw_input()
	if (integer,frac) not in hist:
		hist.add((integer,frac))
		construct_continued_fraction(1/frac,acc,hist)
	return acc[0],acc[1:]
