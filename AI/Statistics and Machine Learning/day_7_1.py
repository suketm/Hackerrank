


import numpy as np
#import pandas as pd



n = int(input())

data = {}
missing_data = {}


for i in range(n+1):
	text = input().split()
	if i > 1:
		text[0] = int(text[0])
		miss = 0
		if text[1] not in data:
			data[text[1]] = {}
		
		if 'Missing' not in text[2]:
			text[2] = float(text[2])
		else:
			missing_data[text[2]] = ('H',text[1],text[0])
			miss = 1
		
		if 'Missing' not in text[3]:
			text[3] = float(text[3])
		else:
			missing_data[text[3]] = ('L',text[1],text[0])
			miss = 1
		text.append(miss)
		data[text[1]][text[0]] = text[2:]

df  = pd.DataFrame(data).transpose()



gap = {d:[] for d in data}
for d in data:
	for k in data[d]:
		if data[d][k][2] == 0:
			gap[d].append(data[d][k][0]-data[d][k][1])

avg_gap = {d: np.mean(gap[d]) for d in gap}


for m in missing_data:
	d = missing_data[m][1]
	k = missing_data[m][2]
	if missing_data[m][0] == 'H':
		missing_data[m] = data[d][k][1] + avg_gap[d]
	else:
		missing_data[m] = data[d][k][0] - avg_gap[d]



for i in range(len(missing_data)):
	print (round(missing_data['Missing_'+str(i+1)],2))