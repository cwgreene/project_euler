#note this would probably work really well as a prolog program

one_pair = "X_ X_ __ __ __"
two_pair = "X_ X_ Y_ Y_ __"
three_of_kind = "X_ X_ X_ __ __"
straight = "X_ (X+1)_ (X+2)_ (X+3)_ (X+4)_"
flush = "_S _S _S _S _S"
full_house = "X_ X_ X_ X_ __"
straight_flush = [flush,straight]
royal_flush = [flush,":X=10"]

def check_hand_single(hand,pattern,domains,constraints):
	local_constraints = list(constraints)
	if pattern[0] == ":": #new constraint
		local_constraints 
	for var,domain in domains:
		for x in domain:
			for constraint in constraints:
				if !satisfies_constraint(
						(var,x),constraint):
					


def check_hand(hand,pattern,domains,constraints=[]):
	if constraints == []:
		constraints = list() #create new empty list
	if type(pattern) == type([]):
		for a_pattern in pattern:
			if not check_hand(hand,a_pattern,
						domains,constraints):
				return False
	else:
		check_hand_single(hand,pattern,domains,constraints)
