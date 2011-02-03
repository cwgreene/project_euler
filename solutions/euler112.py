#Problem 112
#let's just try and brute force it. Most numbers are bouncy.

def is_bouncy(n):
	digits = map(int,str(n))
	sign = 0
	i = 0
	while digits[i] == digits[i+1]:
		i+=1
		if i+1 == len(digits):
			return False
	if digits[i] < digits[i+1]:
		sign = -1
	else:
		sign = 1
	for i in range(i+1,len(digits)):
		if digits[i-1]*sign < digits[i]*sign:
			return True
	return False

def main(percent):
	count = 0#;21780*.9
	n = 99
	while count != percent*n:
		n+=1
		if is_bouncy(n):
			count+=1
	print n

if __name__=="__main__":
	main(.99)
