

''' DFS '''

def make_graph():
	global ls, graph, n
	for i in range(n):
		for j in ls[i]:
			graph[i][j] = 1 
			graph[j][i] = 1


def dfs(vertex, temp):
	global status, n
	status[vertex] = 1
	temp.append(vertex)
	new_vertex_ls = [i for i in range(n) if graph[vertex][i] == 1]
	for new_vertex in new_vertex_ls:
		if status[new_vertex] == 0:
			dfs(new_vertex,temp)


''' Main starts here '''

n = 8
ls = [[] for i in range(n)]
graph = [[0]*n for i in range(n)]
status = [0]*n
graphIdx = ['']*n
subGraph = []

ls[0].append(1)
ls[1].append(4)
ls[2].append(3)
ls[3].append(0)
ls[6].append(2)
ls[6].append(4)
ls[7].append(5)


make_graph()


for vertex in range(n):
	if status[vertex] == 0:
		temp = []
		dfs(vertex, temp)
		for ver in temp:
			graphIdx[ver] = len(subGraph)
		subGraph.append(len(temp))
