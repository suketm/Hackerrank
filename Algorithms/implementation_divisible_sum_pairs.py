
def func(arr, n, k):

	counter = 0

	for i in range(n-1):
		for j in range(i+1,n):
			if (arr[i] + arr[j])%k == 0:
				counter += 1

	return counter




n,k = map(int, input().split())
arr = [int(element) for element in input().split()]

print (func(arr, n, k))