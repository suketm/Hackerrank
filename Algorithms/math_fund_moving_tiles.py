l,s1,s2 = map(float,input().split())
q=int(input())
Q=[]
for i in range(q):
    x=int(input())
    Q.append(x)
for i in range(q):
    print((l-Q[i]**.5)*(2**.5)/(abs(s2-s1)))
