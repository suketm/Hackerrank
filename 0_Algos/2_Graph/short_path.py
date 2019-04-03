
def update(v, nextVer, dist, n):
	graphNew[v][nextVer] = 0
	verList = [i for i in range(n) if (graphNew[nextVer][i] != 0 and i != v)]
	for ver in verList:
		if graphNew[v][ver] != 0:
			d = min(graphNew[v][ver], dist + graphNew[nextVer][ver])
		else:
			d = dist + graphNew[nextVer][ver]
		graphNew[v][ver] = d
		graphNew[ver][v] = d
		graphNew[ver][nextVer] = 0


def dist(v,n):
	
	
	while sum(graphNew[v]) != 0:
		verList = graphNew[v]
		next_verD = [d for d in verList if d != 0]
		d = min (next_verD)
		next_ver = verList.index(d)
		distance[next_ver] = d
		update(v,next_ver,d,n)

	return distance



n = 9
graph =	[[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], \
	[0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7],\
	[0, 0, 2, 0, 0, 0, 6, 7, 0]]

source = 0
graphNew = graph.copy()
distance = ['' if i != 0 else 0 for i in range(n)]
ls_dist = dist(0,n)