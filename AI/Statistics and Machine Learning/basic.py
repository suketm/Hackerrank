
n = int(input())
data = input().split()
for i in range(n):
	data[i] = int(data[i])

data.sort()

mean = sum(data)/n
print (round(mean,1))

if n/2 == n//2:
	print (round((data[n//2]+data[n//2-1])/2,1))
else:
	print (round(data[n//2],1))

data_dict = {d:data.count(d) for d in data}
mode = None
count = 0
for item in data_dict:
	if data_dict[item] > count:
		count = data_dict[item]
		mode = item
	elif data_dict[item] == count:
		if item < mode:
			mode = item
print (mode)

std_dev = (sum([(d-mean)**2 for d in data])/n)**0.5

print (round(std_dev,1))

print (round(mean-1.96*std_dev/(n)**0.5,1),' ',round(mean+1.96*std_dev/(n)**0.5,1))


