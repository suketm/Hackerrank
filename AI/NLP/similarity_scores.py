

from math import log

''' Similarity using TF-Inverse Doc Freq algorithm '''

def term_freq(n):
	for i in range(n):
		tf[i] = {}
		for w in word:
			counter = 0.0
			for temp_word in doc[i]:
				if w == temp_word:
					counter += 1
			tf[i][w] = counter/len(doc[i])


def inv_doc_freq(n):
	for w in word:
		counter = 0
		for d in doc[1:n]:
			if w in d:
				counter += 1
		if counter != 0:
			idf[w] = 1 + log((n-1)/counter)
		else:
			idf[w] = 1


def compute_vector(n):
	for i in range(n):
		vector[i] = {}
		for w in doc[0]:
			vector[i][w] = tf[i][w]*idf[w]


def compute_score(n):
	for i in range(n):
		v1 = 0
		v2 = 0
		v3 = 0
		for w in doc[0]:
			v1 += vector[0][w]*vector[i][w]
			v2 += vector[0][w]*vector[0][w]
			v3  += vector[i][w]*vector[i][w]
		score[i] = v1/(v2*v3)**0.5


# n documents
n = 4
doc = [None]*n
NetScore = [None]*n
word = []

doc[0] = "I would like an apple".split()
doc[1] = "An apple a day keeps the doctor away".split()
doc[2] = "Never compare an apple to an orange".split()
doc[3] = "I prefer scikit-learn to orange".split()

for d in doc:
	for w in d:
		if w not in word:
			word.append(w)

tf = [None]*n
term_freq(n)

idf = {}	# not for a given query; Note: we use all the words - universe of words, including the query but we compute weights from documents
inv_doc_freq(n)

vector = [None]*n
compute_vector(n)

score = [None]*n
compute_score(n)
