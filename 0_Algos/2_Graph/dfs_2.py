



def dfs(v):

	if status[v-1] == 0:
		status[v-1] = 1
		order.append(v)
		for new_vertex in ls[v]:
			dfs(new_vertex)

n = 8

status = [0]*n

order = []

ls = {}
ls[1] = [2,4]
ls[2] = [1,5]
ls[3] = [4,5,7]
ls[4] = [1,3,]
ls[5] = [2,3,7]
ls[6] = [8]
ls[7] = [3,5]
ls[8] = [6]


for v in ls:
	dfs(v)