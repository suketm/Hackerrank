def sort():

	n = len(ls)

	i = 0

	while i < n - 1:
		if ls[i] > ls[i+1]:
			j = i
			while j > -1 and ls[j] > ls[i+1]:
				j -= 1
			j += 1
			temp = ls[i+1]
			ls[j+1:i+2] = ls[j:i+1]
			ls[j] = temp
		i += 1





	





# main

ls = list(open('sort_case.txt','r'))
ls = [int(element.replace('\n','')) for element in ls]
ls = ls[:10000]
ls_original = ls.copy()
ls_sort = ls.copy()
ls_sort.sort()

sort()

print ('Original and New:\t',ls_original == ls)
