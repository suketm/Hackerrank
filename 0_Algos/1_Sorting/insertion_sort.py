
def sort():
	n = len(ls)

	for i in range(1,n):
		key = ls[i]
		
		j = i-1
		while j >= 0 and ls[j] > key:
			ls[j+1] = ls[j]
			j -= 1
		ls[j+1] = key
		print (ls)


ls  = [12, 11, 13, 5, 6]
print (ls)
sort()