import numpy as np
import pandas as pd

n = int(input())

columns = input().split("\t")

years = []
months = []
ttmax = []
ttmin = []

missing = []
for i in range(n):
    l = input().split("\t")

    years.append(int(l[0]))
    months.append(l[1])
    
    #print(l[2])
    if 'Missing' in l[2]:
        ttmax.append(np.nan)
        missing.append([i, "min"])
    else:
        ttmax.append(float(l[2]))
        
    if 'Missing' in l[3]:
        ttmin.append(np.nan)
        missing.append([i, "max"])
    else:
        ttmin.append(float(l[3]))
        
dic = {}
for col, value in zip(columns, [years, months, ttmin, ttmax]):
    dic[col] = value

df = pd.DataFrame(dic)
df=df.interpolate(method="quadratic")
for miss in missing:
    if miss[1] == "min":
        print(round(df.iloc[miss[0]]['tmin'], 1))
    else:
        print(round(df.iloc[miss[0]]['tmax'], 1))
