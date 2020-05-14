
b, n, m = map(int, input().split())
keyboard = [int(element) for element in input().split()]
drive = [int(element) for element in input().split()]

if min(keyboard) + min(drive) > b:
	print (-1)
else:
	keyboard.sort(reverse = True)
	drive.sort(reverse = True)

	k = 0
	while k < n:
		balance = b - keyboard[k]
		d = 0
		while balance >


https://www.hackerrank.com/challenges/electronics-shop/problem