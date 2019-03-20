


import matplotlib.pyplot as plt
import numpy as np

n = int(input())

num = []

for i in range(n):
	passenger_num = input().split()
	num.append(int(passenger_num[1]))




# solution: 1: create pdf, use prob to produce simillar sample

(freq,bins) = np.histogram(num, bins = 10)

probs = [f/len(num) for f in freq]
bins_ = [ (bins[i] + bins[i+1])/2 for i in range(10)]

num_1 = []
for i in range(12):
	num_1.append(int(round(np.random.choice(bins_, p=probs))))
	print (num_1[-1])


# Solution: 2: Use time series model: 
from pandas import Series
from statsmodels.tsa.arima_model import ARIMA

series = Series(num)
bias = 1164767.0
model = ARIMA(series.values, order=(6,2,0))

model_fit = model.fit(trend = 'nc', disp = 0)
forecast = bias + model_fit.predict(start = 60, end = 71)

for value in forecast:
	print int(value)


# Solution No. 3:

from scipy import interpolate
leng = list(range(len((num))))
interpolation = interpolate.interp1d(leng,num,fill_value='extrapolate')

y = interpolation(range(len(num),len(num)+12))
        
for x in y:
    print(x)