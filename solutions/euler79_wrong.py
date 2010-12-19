import sys

def new_min(oldmin,newinfo):
	substr = oldmin
	newmin = oldmin
	for i,x in enumerate(newinfo):
		if x in substr:
			substr = substr[substr.index(x):]
		else:
			break
	if i != len(newinfo)-1:
		newmin += newinfo[i:]
	return newmin

def main(filename):
	entries = open(filename)
	min = ""
	for line in entries:
		new_entry = line.strip()
		min = new_min(min,new_entry)
		print min,"(",new_entry,")"

if __name__=="__main__":
	main(sys.argv[1])
