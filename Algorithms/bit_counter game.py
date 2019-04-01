

from math import log


def solve(n):
	global counter
	counter += 1
	if n > 1:
		x = int(log(n,2))
		if 2**x == n:
			n /= 2
			solve(n)
		else:
			n = n - 2**x
			solve(n)


t = int(input())

name = {1:'Louise',2:'Richard'}
ans = []

for i in range(t):
	n = int(input())
	counter = 0
	solve(n)
	if counter//2 == counter/2:
		ans.append(name[1])
	else:
		ans.append(name[2])


for a in ans:
	print (a)