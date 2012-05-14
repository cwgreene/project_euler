def get_triangles(filename):
	triangles = []
	for line in open(filename):
		values = map(int,line.strip().split(','))
		pairs = zip(values[:-1:2],values[1::2])
		triangles.append(pairs)
	return triangles

def cross(vec1,vec2):
	z = vec1[0]*vec2[1]-vec1[1]*vec2[0]
	return z

def sign(x):
	if x > 0:
		return 1
	if x == 0:
		return 0
	if x < 0:
		return -1

def all_same(alist):
	first = alist[0]
	for x in alist[1:]:
		if x != first:
			return False
	return True
	
def contains_point(poly,point):
	poly = [(x[0]-point[0],x[1]-point[1]) for x in poly]
	vecpairs = zip(poly[:],[poly[-1]]+poly[:-1])
	signs = map(lambda x: sign(cross(*x)),vecpairs)
	if all_same(signs):
		return True
	return False

triangles = get_triangles("data/triangles.txt")
count = 0
for tri in triangles:
	#vecpairs = zip(tri[:],[tri[-1]]+tri[:-1])
	#signs = map(lambda x: sign(cross(*x)),vecpairs)
	#print signs
	#if signs[0] == signs[1] == signs[2]:
	if contains_point(tri,[0,0]):
		count += 1
print count
