coef = 28433
exp = 7830457

def fast_mod_exp(base,exp,mod,depth = 1):
	if exp == 1:
		return base
	if exp %2 == 0:
		return fast_mod_exp(base*base,exp/2,mod,depth)%mod
	return base*fast_mod_exp(base,exp-1,mod,depth+1) % mod

print (coef*fast_mod_exp(2,exp,10**10)%10**10)
