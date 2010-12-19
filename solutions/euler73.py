#walk from the end to the start
from euler71 import predecessor,predecessor_slow,euler_phi,predecessor_count

def walk(start,finish,maxdenom):
	walk = [start]
	current = start
	while (current != finish):
		current = predecessor(current[0],current[1],maxdenom)
		#print current
		walk.append(current)
	return walk

#less memory intensive
def walk_count(start,finish,maxdenom):
	count = 1
	current = start
	while (current != finish):
		current = predecessor(current[0],current[1],maxdenom)
		#print current
		count += 1
	return count

def main():
	#walk((1,2),(1,3),8)
	for x in range(12000+1):
		euler_phi(x)
	print x
	print predecessor_count(1,2,1,3,12000)
	#print walk_count((1,2),(1,3),1000)-2
if __name__ == "__main__":
	main()
