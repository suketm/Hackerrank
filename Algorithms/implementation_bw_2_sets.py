
def func(a, b, n, m):

	min_elem = max(a)
	max_elem = min(b)

	ans = []
	for i in range(min_elem, max_elem+1):
		j = 0
		while j < n and i%a[j] == 0:
			j += 1
		if j == n:
			if i%a[j-1] == 0:
				
				k = 0
				while k < m and b[k]%i == 0:
					k += 1

				if k == m:
					if b[k-1]%i == 0:
						ans.append(i)

	return (ans)


n,m = map(int, input().split())
a = [int(element) for element in input().split()]
b = [int(element) for element in input().split()]

print (func(a,b,n,m))