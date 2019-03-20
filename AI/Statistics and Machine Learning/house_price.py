
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression
import numpy as np

f,n = map(int,input().split())

features = []
price = []

for i in range(n):

	text = input().split()
	for i in range(f+1):
		text[i] = float(text[i])
	features.append(text[:-1])
	price.append(text[-1])


t = int(input())

features2 = []

for j in range(t):
	text = input().split()
	for i in range(f):
		text[i] = float(text[i])
	features2.append(text)


def test(deg):

	poly = PolynomialFeatures(degree = deg)
	X_poly = poly.fit_transform(features)
	wt = np.linalg.lstsq(X_poly,price, rcond = None)[0]

	X_poly2 = poly.fit_transform(features2)
	print ('\n')
	print ('Degree:',deg)
	for j in range(t):
		print (round(sum(X_poly2[j]*wt),2))


for i in range(5):
	test(deg = i)