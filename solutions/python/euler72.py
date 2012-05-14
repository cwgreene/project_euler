#This problem could be done in mathematica very trivially
#Sum[EulerPhi[n],{n,2,1 000 000}]
#
#So we just need the euler_phi function efficiently implemented.

import primes

def main():
	primes.init(1000*1000+10)
	cur = 2
	total = 0
	while cur <= 1000*1000:
		total+= int(primes.euler_phi(cur))
		if cur % 1000 == 0: print cur
		if total < 0:
			print type(total),type(cur)
			break
		cur +=1
	print total

if __name__=="__main__":
	main()
