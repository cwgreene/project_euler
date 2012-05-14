from graph import dijkstra

def matrix_graph(n,m,values):
	graph = {}
	for x in range(1,n+1):
		for y in range(1,m+1):
			graph[(x,y)] = []
			if y > 1: #connected to above
				pos = x,y-1
				val = values[pos]
				graph[(x,y)].append( (pos,val) )
			if y < m: #connected to down
				pos = x,y+1
				val = values[pos]
				graph[(x,y)].append( (pos,val) )
			if x < n: #connected to right
				pos = x+1,y
				val = values[pos]
				graph[(x,y)].append( (pos,val) )
			if x > 1: 
				pos = x-1,y
				val = values[pos]
				graph[(x,y)].append( (pos,val) )
	return graph

def parse_file(file):
	lines = open(file).readlines()
	values = {}
	for y,line in enumerate(lines):
		for x,num in enumerate(line.strip().split(",")):
			values[(x+1,y+1)] = int(num)
	return values

def solve(file):
	values = parse_file(file)
	ymax = max([value[1] for value in values.keys()])
	xmax = max([value[0] for value in values.keys()])
	print "max:",xmax,ymax
	graph = matrix_graph(xmax,ymax,values)
	dresult = dijkstra(graph,(1,1))
	print values[(1,1)]+dresult[(xmax,ymax)]

solve("data/matrix.txt")
