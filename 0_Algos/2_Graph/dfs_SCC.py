'''
	A directed graph is called strongly connected if there is a path in each direction between each pair of vertices 
	of the graph. That is, a path exists from the first vertex in the pair to the second, and another path exists from 
	the second vertex to the first. In a directed graph G that may not itself be strongly connected, a pair of vertices
	u and v are said to be strongly connected to each other if there is a path in each direction between them.
'''

def dfs(v, ls_temp):
	status[v] = 1
	d = [v]
	for new_vertex in ls_temp[v]:
		if status[new_vertex] == 0:
			d += dfs(new_vertex,ls_temp)
	return d

def rev_graph(n):
	ls_rev = {new_vertex:[] for new_vertex in range(n)}
	for v in ls:
		for new_vertex in ls[v]:
			if v not in ls_rev[new_vertex]:
				ls_rev[new_vertex] += [v]
	return ls_rev

n = 8
ls = {}
scc = []

ls[0] = [1]
ls[1] = [2]
ls[2] = [0,3]
ls[3] = [5,6]
ls[4] = [3]
ls[5] = [4]
ls[6] = [7]
ls[7] = []

t1 = []
status = [0]*n
for v in range(n):
	if status[v] == 0:
		t1 += dfs(v,ls)

ls_rev = rev_graph(n)

status = [0]*n
for v in t1:
	if status[v] == 0:
		scc.append(dfs(v,ls_rev))
