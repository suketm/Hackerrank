
# Quick sort

def quick_sort(ls,low,high):

	if high - low > 0:

		pivot = ls[low]
		idx = low

		for i in range(low+1,high+1):

			if ls[i] < pivot:
				idx += 1
				ls[idx], ls[i] = ls[i], ls[idx]
		
		ls[low], ls[idx] = ls[idx], ls[low]
		quick_sort(ls,low,idx-1)
		quick_sort(ls,idx+1,high)



''' Main Starts '''

ls = []
n = int(input())

for i in range(n):
	ls.append(int(input()))

quick_sort(ls,0,n-1)