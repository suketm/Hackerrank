
#!/bin/python3

n,k = map(int, input().split())

arr = [int(element) for element in input().split()]

print (len(set(arr) & set(x + k for x in arr)))