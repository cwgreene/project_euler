from collections import defaultdict

def octagonal(n):
	return n*(3*n-2)
def heptagonal(n):
	return n*(5*n-3)/2
def hexagonal(n):
	return n*(2*n-1)
def pentagonal(n):
	return n*(3*n-1)/2
def square(n):
	return n*n
def triangle(n):
	return n*(n+1)/2

def generate_four_digits(function):
	n = 1
	while function(n) < 1000:
		n+=1
	result = defaultdict(list) 
	while function(n) < 10000:
		funcval = function(n)
		valstr = str(funcval)
		result[valstr[0:2]].append(str(function(n)))
		n+=1
	return result

def generate_sequence(cur_remaining,curkey):
	results = []
	for numtype in cur_remaining:
		if curkey in numtype: #can we match?
			rem = list(cur_remaining)
			rem.remove(numtype)
			if rem == []: #at end
				for num in numtype[curkey]:
					results.append([num])
			for num in numtype[curkey]:
				subsq = generate_sequence(rem,num[2:])
				for x in subsq:
					if x != []:
			 		 for num in numtype[curkey]:
					  results.append([num]+x)
	return results #could be empty

def main():
	all_funcs = [triangle,square,pentagonal,
			hexagonal,heptagonal,octagonal]
	all_digits = map(generate_four_digits,all_funcs)
	for value in all_digits[0].values():
		for num in value:
			results = generate_sequence(all_digits[1:],num[2:])
			for result in results:
				if num[0:2] == result[-1][2:]:
					print sum(map(int,[num]+result))

if __name__=="__main__":
	main()
