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

def round(n,k):
	num = math.floor(n*k)/k
	return num

def next_num(radical,numer,denom,integer):
	sub = integer*denom
	denom = denom-integer*denom
	

def eval_num(radical,numer,denom):
	return int(math.floor((math.sqrt(radical)-numer)/denom))

def construct_continued_fraction(num,acc=None,hist=None):
	if acc == None: acc = []
	if hist == None: hist = set()
	radical,numer,denom=num
	integer = eval_num(radical,numer,denom)
	acc.append(integer,integer)
	if (integer,rcoef,coef) not in hist:
		hist.add((integer,rcoef,coef))
		nextnum = next_num(radical,numer,denom,integer)
		construct_continued_fraction(nextnum,acc,hist)
	return acc[0],acc[1:]
#the following, as one would expect does not work
#if num is not a float due to rounding
#So either tolerance must be introduced
#(which makes the dict approach mostly untenable)
#or the remainder most be made exact. This is doable
#for the purposes of roots
#or we can just round the key...
def construct_continued_fraction_wrong(num,acc=None,hist=None):
	if acc == None: acc = []
	if hist == None: hist = set()
	integer,frac = math.floor(num),num-math.floor(num)
	places = 10**4
	if (integer,round(frac,places)) not in hist:
		acc.append(integer)
		hist.add((integer,round(frac,places)))
		construct_continued_fraction_wrong(1/frac,acc,hist)
	return acc[0],acc[1:]

def main(n):
	count = 0
	for x in range(1,n+1):
		sqrtx = math.sqrt(x)
		if sqrtx*sqrtx != x:
			result=construct_continued_fraction_wrong(sqrtx)
			start,pattern = result
			if len(pattern) % 2 != 0:
				count +=1
	print count

if __name__=="__main__":
	main(10**4)
