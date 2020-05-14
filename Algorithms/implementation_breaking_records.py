

def func(scores, n):

	min_val = scores[0]
	max_val = scores[0]

	ans = [0,0]
	for i in range(1, n):
		if scores[i] < min_val:
			ans[1] += 1
			min_val = scores[i]
		elif scores[i] > max_val:
			ans[0] += 1
			max_val = scores[i]
	
	return ans



n = int(input())
scores = [int(element) for element in input().split()]

for val in func(scores, n):
	print (val, end = ' ')





'''
9
10 5 20 20 4 5 2 25 1

10 (0,0)
5 (1,0)
20 (1,1)
20 (1,1)
4
5
2
25 (,2)
1

2 4
'''