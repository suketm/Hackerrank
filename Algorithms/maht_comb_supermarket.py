from fractions import gcd

def lcm(a,b):
    return a / gcd(a,b) * b

n = input()

bitcount = [0]*(1<<n)
lcms = [1]*(1<<n)
for i in xrange(n):
    a = input()
    for j in xrange(1<<i):
        lcms[(1<<i)|j] = lcm(a, lcms[j])
        bitcount[(1<<i)|j] = bitcount[j] + 1

def count(k):
    t = 0
    for s in xrange(1,1<<n):
        t -= k / lcms[s] * (-1)**bitcount[s]
    return t

for i in xrange(input()):
    l, r = map(int, raw_input().strip().split())
    print count(r) - count(l-1)
