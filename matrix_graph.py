import networkx as nx

def matrix_to_graph(matrix):
	graph = nx.DiGraph()
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			graph.add_node((i,j))
			if i > 0:
				graph.add_edge((i-1,j),(i,j),	
						data=int(matrix[i][j]))
			if j > 0:
				graph.add_edge((i,j-1),(i,j),
						data=int(matrix[i][j]))
	return graph

def construct_matrix(astr):
	rows = astr.split("\n")
	return map(lambda x:x.split(","),rows)
