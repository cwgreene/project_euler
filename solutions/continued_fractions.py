from fractions import Fraction as Fr

def rotshift(alist):
	return alist[1:]+alist[0:1]

def evaluate_continued_fraction(frac,n):
	a0,reps = frac
	if n == 0:
		return a0*Fr(1)
	acc = a0
	acc += 1/(reps[0]+evaluate_continued_fraction((0,rotshift(reps)),n-1))
	return acc

