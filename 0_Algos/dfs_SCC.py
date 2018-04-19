
''' dfs with topological order '''

def reverse(ls,ls2,n):
	for i in range(n):
		for j in ls[i]:
			ls2[j].append(i)

def dfs (ls,que,stat,vertex):
	stat[vertex] = 1
	que.insert(0,vertex)
	for new_vertex in ls[vertex]:
		if stat[new_vertex] == 0:
			dfs(ls,que,stat,new_vertex)

# Main starts...
n = 5
ls = [[] for i in range(n)]		# graph
status = [0]*n
queue = []
ls2 = [[] for i in range(n)]		# graph

# graph(ls) , function: to input graph. In this case, we will do it manually.
ls[0].append(2)
ls[0].append(3)
ls[1].append(0)
ls[2].append(1)
ls[3].append(4)

for vertex in range(n):
	if status[vertex] == 0:
		dfs(ls,queue,status,vertex)

reverse(ls,ls2,n)
status2 = [0]*n
while queue != []:
	vertex = queue.pop()
	scc = []
	if status2[vertex] == 0:
		dfs(ls2,scc,status2,vertex)
		print scc