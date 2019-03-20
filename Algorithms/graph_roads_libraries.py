
''' Question based on dfs '''
''' Only 2 cases; solve using x and y; we will end up with a condition such that only cases are permissible '''

def dfs(graph, vertex, temp, status, n):
	status[vertex] = 1
	temp.append(vertex)
	new_vertex_ls = graph[vertex]				#[i for i in range(n) if graph[vertex][i] == 1]
	for new_vertex in new_vertex_ls:
		if status[new_vertex] == 0:
			dfs(graph,new_vertex,temp,status,n)


def compute_cost(graph, n, cLib, cRoad):
	cost = 0
	status = [0]*n
	for vertex in range(n):
		if status[vertex] == 0:
			x = []
			temp = []
			dfs(graph,vertex,temp,status,n)
			cost += cLib + cRoad*(len(temp)-1)
	return cost

''' Main Starts '''

cost = []
numQuerry = int(input())

for querry in range(numQuerry):
	n , m , cLib, cRoad = map(int, input().split())
	graph = [[] for j in range(n)]
	while m > 0:
		x, y = map(int,input().split())
		graph[x-1].append(y-1)
		graph[y-1].append(x-1)
		m -= 1
	if cLib < cRoad:
		cost.append(n*cLib)
	else:
		cost.append(compute_cost(graph, n, cLib,cRoad))

for c in cost:
	print (c)
