
''' dfs with topological order '''



def dfs(v):
	status[v] = 1
	for new_vertex in ls[v]:
		if status[new_vertex] == 0:
			dfs(new_vertex)
	order.insert(0,v)


n = 6
order = []
status = [0]*n
ls = {}
ls[0] = []
ls[1] = []
ls[2] = [3]
ls[3] = [1]
ls[4] = [0,1]
ls[5]= [2,0]


for v in [4,0,1,2,3,5]:
	if status[v] == 0:
		dfs(v)
