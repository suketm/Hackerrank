
n = int(input())
arr = [int(element) for element in input().split()]

freq = [arr.count(sock)//2 for sock in set(arr)]

print (sum(freq))
