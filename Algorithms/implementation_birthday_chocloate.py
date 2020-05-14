
def func(arr, n, d, m):

	counter = 0

	for i in range(m-1, n):

		if sum(arr[i-m + 1 : i+1]) == d:
			counter += 1
	
	return (counter)



n = int(input())
arr = [int(element) for element in input().split()]
d, m = map(int, input().split())

print (func(arr, n, d, m))