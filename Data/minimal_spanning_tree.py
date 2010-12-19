#problem 107
import networkx as nx

def load_graph_from_table(filename):
	afile = open(filename)
	matrix = map(lambda x: (x.strip()).split(','),afile.read().split("\n"))
	matrix = matrix[:-1] #get rid of newline
	G = nx.DiGraph()
	for id in range(len(matrix)):
		G.add_node(id)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			val = matrix[i][j]
			if val != '-':
				G.add_edge(i,j,data=int(val))
	return G
