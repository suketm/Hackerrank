
import sys

def para_sent(text):
	i = 0
	start = 0
	quote = 0
	punch_list = ['?','!','.']
	while i < len(text):
		if text[i] == '"':
			quote += 1
		elif text[i] in punch_list and quote%2 == 0:
			ls.append(text[start:i])
			j = len(text)
			for j in range(i+1,len(text)):
				if text[j] != ' ':
					break
			start = j
		i = max(start,i+1)


def trigram():
	for line in ls:
		temp = line.split()
		for j in range(len(temp)-2):
			word = temp[j].lower() +' '+ temp[j+1].lower() +' '+ temp[j+2].lower()
			if word in list(tri.keys()):
				tri[word] += 1
			else:
				tri[word] = 1
				if rank != {}:
					rank[word] = max(list(rank.values())) + 1
				else:
					rank[word] = 1
	max_freq = max(list(tri.values()))
	ls_max_tri = []
	for t in tri:
		if tri[t] == max_freq:
			ls_max_tri.append(t)
	ans = ls_max_tri[0]
	r = rank[ans]
	for t in ls_max_tri:
		if rank[t] < r:
			ans = t
			r = rank[t]
	return (ans)

''' NLP trigram '''

text = sys.stdin.read().strip()
ls = []
tri = {}
rank = {}

para_sent(text)

# detect trigram

ans = trigram()

print (ans)