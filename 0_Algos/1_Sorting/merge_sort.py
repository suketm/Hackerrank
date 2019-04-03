# merge sort



def merge(ls1, ls2):
	n1 = len(ls1)
	n2 = len(ls2)
	ls_temp2 = []
	i = 0
	j = 0
	while i != n1 or j != n2:
		if i < n1 and j < n2:
			if ls1[i] < ls2[j] or ls1[i] == ls2[j]:
				ls_temp2.append(ls1[i])
				i += 1
			elif ls1[i] > ls2[j]:
				ls_temp2.append(ls2[j])
				j += 1
		elif i == n1 and j < n2:
			ls_temp2 += ls2[j:n2]
			j = n2
		elif j == n2 and i < n1:
			ls_temp2 += ls1[i:n1]
			i = n1
	return ls_temp2


def sort(ls_temp):
	if len(ls_temp) > 2:
		n = len(ls_temp)
		ls_temp1 = sort(ls_temp[0:n//2])
		ls_temp2 = sort(ls_temp[n//2:n])
		ls_temp = merge(ls_temp1, ls_temp2)
	elif len(ls_temp) == 2:
		if ls_temp[0] > ls_temp[1]:
			ls_temp[0],  ls_temp[1] = ls_temp[1],  ls_temp[0]
	return ls_temp


''' Main Starts '''

x = list(open('sort_case.txt','r'))
n = len(x)
x = [ int(x[i].replace('\n','')) for i in range(n)]


ls = x.copy()


ls = sort(ls)
x.sort()
print (ls == x)
