for _ in range(int(input())):
    n,d = [int(temp) for temp in input().split()]
    loop = n // d
    r = n % d
    pair = d * (loop - 1) * loop // 2 + (r + (d - 1) // 2) * loop
    if r > d // 2:
        pair += r - d // 2
    print(pair)
