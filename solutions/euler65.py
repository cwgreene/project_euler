#euler 65

import continued_fractions as cf

def generate_e_seq(n):
	result = [2]
	reps = []
	for i in range(1,n+1):
		if  i % 3 == 2:
			reps.append(2*(i/3+1))
		else:
			reps.append(1)
	result.append(reps)
	return result

hundredth = cf.evaluate_continued_fraction(generate_e_seq(100),99)
print sum(map(int,str(hundredth.numerator)))
