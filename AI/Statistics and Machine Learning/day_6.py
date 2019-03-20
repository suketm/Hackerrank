
import numpy as np

X = []
y = []
X_ = []
y_ =[]

F, n1 = map(int, input().split())

for i in range(n1):
	temp = list(map(float,input().split()))

	X.append(temp[:-1] + [1])
	y.append(temp[-1])


wt = np.linalg.lstsq(X,y, rcond = None)[0]

n2 = int(input())


for i in range(n2):
	temp = list(map(float,input().split()))
	X_.append(temp)
	y_.append(sum((temp+[1])*wt))

for i in range(n2):
	print (y_[i])
