
n,k = map(int, input().split())
bill = [int(element) for element in input().split()]
b = int(input())

bill[k] = 0

fair_val = sum(bill)/2

if fair_val == b:
	print ('Bon Appetit')
else:
	print (round(b - fair_val))