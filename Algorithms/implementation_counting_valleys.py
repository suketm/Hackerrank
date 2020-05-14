
n = int(input())
s = [1 if element == 'U' else -1 for element in input()]


counter = 0
status = 0

step = 0
while step < n:
	if status == 0 and s[step] == -1:
			status = 1
			start_pt = step
			step += 1
			sum_val = -1
			while step < n and status != 0:
				sum_val += s[step]
				if sum_val == 0:
					counter += 1
					status = 0
				step += 1
	elif status == 0 and s[step] == 1:
		status = -1
		start_pt = step
		step += 1
		sum_val = 1
		while step < n and status != 0:
			sum_val += s[step]
			if sum_val == 0:
				status = 0
			step += 1


print (counter)