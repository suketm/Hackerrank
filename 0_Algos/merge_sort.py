# merge sort

def merge (ls, ls1, ls2):

	idx1 = 0
	idx2 = 0
	n = len(ls)
	n1 = len(ls1)
	n2 = len(ls2)

	for i in range(n):

		if idx1 < n1 and idx2 < n2:
			if ls1[idx1] < ls2[idx2]:
				ls[i] = ls1[idx1]
				idx1 +=1
			else:
				ls[i] = ls2[idx2]
				idx2 +=1

		elif idx1 == n1:
			ls[i:n] = ls2[idx2:n2]
			break

		elif idx2 == n2:
			ls[i:n] = ls1[idx1:n1]
			break

def merge_sort(ls):

	if len(ls) > 2:

		n = len(ls)

		ls1 = ls[0:int(n/2)]
		ls2 = ls[int(n/2):n]

		merge_sort(ls1)
		merge_sort(ls2)
		merge(ls,ls1,ls2)


	elif len(ls) == 2 and ls[0] > ls[1]:

		ls[0], ls[1] = ls[1], ls[0]

''' Main Starts '''

ls = []

for i in range(n):
	ls.append(int(input()))

merge_sort(ls)
