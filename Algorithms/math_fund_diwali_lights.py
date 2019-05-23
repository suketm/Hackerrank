
t = int(input())

ls = []

for i in range(t):
    ls.append(int(input()))

for i in ls:
    print ((2**i - 1)%10**5)
