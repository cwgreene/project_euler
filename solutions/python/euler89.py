def promote(a,b,c,counts):
	counts[b] += counts[a]/5
	counts[a] %= 5
	if c != None:
		if counts[a] == 4:
			if counts[b] != 0:
				counts[b] -=1
			counts[a] = 9

def invertdict(adict):
	newdict = {}
	for k,v in adict:
		newdict[v] = k
	return newdict

def minimal(romanstring):
	counts = {}
	order = list("IVXLCDM")
	successors = {"I":{"V":4,"X":9},
			"X":{"L":4,"C":9},
			"C":{"D":4,"M":9}}
	successors2 = {"I":{4:"V",9:"X"},
			"X":{4:"L",9:"C"},
			"C":{4:"D",9:"M"}}
	sorder = ['X',None,'C',None,'M',None,None]
	result = ""
	for numeral in order:
		counts[numeral] = 0
	for numeral,next in zip(romanstring,romanstring[1:]+" "):
		if numeral in successors:
			if next in successors[numeral]:
			bonus = successors[numeral][next]
				counts[numeral]+=successors[numeral][next]
				counts[successors2[numeral][next]]-=1
			else:
				counts[numeral] += 1
		else:
			counts[numeral] += 1
	for numeral,next,ten in zip(order[:-1],order[1:],sorder):
		promote(numeral,next,ten,counts)
	reverseorder = list(order[::-1])

	print romanstring,counts
	for numeral,prev in zip(reverseorder, [None]+reverseorder[:-1]):
		if numeral == "M" or (counts[numeral] not in [4,9]):
			result += numeral*counts[numeral]
		elif counts[numeral] == 9:
			result += numeral+successors2[numeral][9]
		else:
			result += numeral+successors2[numeral][4]
	return result
file = open("data/roman.txt")
saved = 0
for line in file:
	line = line.strip()
	#print line,minimal(line),len(line)-len(minimal(line))
	saved += len(line)-len(minimal(line))
print saved
