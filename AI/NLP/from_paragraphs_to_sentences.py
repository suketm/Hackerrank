
def para_sent(text):
	i = 0
	start = 0
	quote = 0
	punch_list = ['?','!','.']
	while i < len(text):
		if text[i] == '"':
			quote += 1
		elif text[i] in  punch_list and quote%2 == 0:
			ls.append(text[start:i+1])
			for j in range(i+1,len(text)):
				if text[j] != ' ':
					break
			start = j
		i = max(start,i+1)


''' NLP Para to Sentence '''

text = input().strip()
ls = []

para_sent()

for line in ls:
    print (line)
