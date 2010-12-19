def is_palindrome(x):
	x=list(str(x))	
	if len(x) % 2 == 0:
		midway = len(x)/2
	else:
		midway = len(x)/2+1
	for a,b in zip(x[:midway],reversed(x[midway:])):
		if a != b:
			return False
	return True
def base2(x):
    z = list(hex(x).upper())
    result = ""
    z.reverse()
    z = z[:z.index('X')]
    for i in z:
        result = "".join(map(str,hexdigitbinary[i]))+result
    return stripleadingzeros(result)

def stripleadingzeros(x):
    z = x
    while '0' in z and z.index('0') == 0:
        z = z[1:]
    return z
