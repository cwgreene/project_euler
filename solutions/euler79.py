#we attempt to do a
#backtracking like solution with a priority queue
import Queue

#return all ordered n choices from m options.
def choose_ordered(n,m):
	for x in range(n):
		

def addcode(curval,subcode)
	#if subcode _matches_ then we don't need to do anything unusual.
	for i,x in enumerate(subcode);
		if x in curval:
			curval = curval[curval.index(x):]
		else
			break
	remaining = subcode[i:]
	results = []
	for index in choose_ordered(2,3):
	

def main():
	bestqueue = Queue.PriorityQueue()
	subcodes = []
	for line in file:
		subcodes.append(line.strip())
	done = False
	while not done:
		curval,index = bestqueue.get()
		curlist = subcodes[i:]
		for i,subcode in enumerate(curlist):
			nextvals,consumed = addcode(str(curval),subcode)
			for nextval in nextvals:
				bestqueue.put((nextval,index+(i+1)))
	return best
		
