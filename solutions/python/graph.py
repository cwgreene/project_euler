from Queue import PriorityQueue as PriQ

def dijkstra(graph,source):
	queue = []
	costs = {source:0}
	visited  = set()
	next = PriQ()
	next.put((0,source))

	while not next.empty():
		cur_node = next.get()[1]
		if cur_node in visited:
			continue
		for node,cost in graph[cur_node]:
			if node not in visited:
				newcost = costs[cur_node]+cost
				if node not in costs:
					costs[node] = newcost
				else:
					if costs[node] > newcost:
						costs[node]=newcost
				next.put((costs[node],node))
		visited.add(cur_node)
	return costs
