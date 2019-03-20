
from math import log

''' NLP: tf-idf '''

def termFreq( doc ):
	tempDict = {}
	temp = doc.split()
	for w in word:
		tempDict[w] = float(temp.count(w))/len(temp)
	return tempDict

def inverseDocFreq (doc1, doc2, doc3):
	idf = {}
	for w in word:
		counter = 0
		for doc in [doc1, doc2, doc3]:
			if w in doc:
				counter += 1
		if counter != 0:
			idf[w] = 1 + log(len([doc1, doc2, doc3])/counter)
		else:
			idf[w] = 1
	return idf

def vector (tf):
	v = []
	for w in word:
		v.append(tf[w]*idf[w])
	return v

def cosSimilarity(temp_vec, vec):
	num = 0
	den1 = 0
	den2 = 0
	for i in range(len(vec)):
		if vec[i] != 0:
			num += vec[i]*temp_vec[i]
			den1 += vec[i]**2
			den2 += temp_vec[i]**2
	return num/(den1*den2)**.5


querry = "life learning"
doc1 = "the game of life is a game of everlasting learning"
doc2 = "the unexamined life is not worth living"
doc3 = "never stop learning"

word = []				# create total list of words

for d in [doc1, doc2, doc3] + [querry]:
	 for key in d.split():
	 	if key not in word:
	 		word.append(key)


tf1 = termFreq(doc1)
tf2 = termFreq(doc2)
tf3 = termFreq(doc3)
tfq = termFreq(querry)

idf = inverseDocFreq(doc1, doc2, doc3)

vector1 = vector(tf1)
vector2 = vector(tf2)
vector3 = vector(tf3)
vectorq  = vector(tfq)

cosSim1 = cosSimilarity(vector1, vectorq)
cosSim2 = cosSimilarity(vector2, vectorq)
cosSim3 = cosSimilarity(vector3, vectorq)

print (cosSim1, cosSim2, cosSim3)