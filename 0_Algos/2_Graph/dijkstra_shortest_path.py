
''' Dijkstra's shortest path '''
import numpy as np

def min_dist(arr,n):

	dist = 0
	idx = 0

	for i in range(n):
		if arr[i] != 0:
			idx = i
			dist = arr[i]
			break

	for i in range(idx,n):
		if arr[i] != 0:
			if arr[i] < dist:
				idx = i
				dist = arr[i]

	return idx, dist


def shortest_path (arr,n,src,sptSet):

	new_src, dist = min_dist(arr[0,:],n)
	sptSet[new_src] = dist
	src.append(new_src)
				
	new_node_idx = [i for i in range(1,n) if arr[new_src,i] !=0]
		
	for i in range(n):
		arr[i,new_src] = 0

	for new_node in new_node_idx:
		if (arr[0,new_node] == 0) or (int(arr[0,new_node]) > dist + int(arr[new_src,new_node])):
			arr[0,new_node] = dist + int(arr[new_src,new_node])

	if len(src) != n :
		shortest_path(arr,n,src,sptSet)

# Main starts... 

n = 9 
sptSet = ['']*n
starting_src = 0		#keep source index always 0

# graph(ls) , function: to input graph. In this case, we will do it manually. Don't keep 0 distance for disconnected pt.s 
arr = np.array(( [0, 4, 0, 0, 0, 0, 0, 8, 0],[4, 0, 8, 0, 0, 0, 0, 11, 0],[0, 8, 0, 7, 0, 4, 0, 0, 2], \
				[0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], \
				[0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0] ))


src = [starting_src]
sptSet[starting_src] = 0

shortest_path(arr,n,src,sptSet)
print (sptSet)
