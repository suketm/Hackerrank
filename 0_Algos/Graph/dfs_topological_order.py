
''' dfs with topological order '''


def dfs_top_order(ls,vertex,status,stack):
	
	status[vertex] = 1
	for new_vertex in ls[vertex]:
		if status[new_vertex] == 0:
			dfs_top_order(ls,new_vertex,status,stack)
	stack.insert(0,vertex)


# Main starts... 
n=6
ls=[[] for i in range(n)]		# graph
status=[0]*n
stack=[] 

# graph(ls) , function: to input graph. In this case, we will do it manually.
ls[2].append(3)
ls[3].append(1)
ls[4].append(0)
ls[4].append(1)
ls[5].append(0)
ls[5].append(2)



for vertex in range(n):
	if status[vertex] == 0:
		dfs_top_order(ls,vertex,status,stack)
