
def bfs(v):
	if status[v-1] == 0:
		status[v-1] = 1
		order.append(v)

		queue = []
		for new_vertex in ls[v]:
			if status[new_vertex-1] == 0:
				status[new_vertex-1] = 1
				order.append(new_vertex)
				queue += ls[new_vertex]
		for q in queue:
			bfs(q)


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
	bfs(v)

