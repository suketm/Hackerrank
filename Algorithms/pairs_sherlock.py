
#!/bin/python3


def func(arr, n):
    i = 0
    t_sum = sum(arr)
    left_sum = 0
    while i < n:
        if i >= 1:
            left_sum += arr[i-1]
        if left_sum == (t_sum - left_sum - arr[i]):
            return 'YES'
        i += 1
    return 'NO'


t = int(input())
ans = []
for i in range(t):
    n = int(input())
    arr = [int(element) for element in input().split()]
    ans.append(func(arr,n))


for a in ans:
    print (a)