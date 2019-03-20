import random

def die_number():
    randRoll = random.random()
    sum_ = 0
    result = 1
    for p in probs:
        sum_ += p
        if randRoll < sum_:
            return result
        result+=1

def die_roll():
	status = 0
	i = 0
	block_number = 1

	while i < 1001 and block_number < 100:
		die_num = die_number()
		temp = die_num +  block_number
		if temp > 100:
			None
		elif temp in snakes:
			block_number = snakes[temp]
		elif temp in ladder:
			block_number = ladder[temp]
		else:
			block_number = temp
		i += 1

	if block_number == 100:
		status = 1

	return status, i


def compute_expected_rolls():

	num_rolls = []

	while len(num_rolls) < 5000:
		status, num_die_roll = die_roll()
		if status == 1:
			num_rolls.append(num_die_roll)
	return (sum(num_rolls)/5000)




t = int(input())
ans = []

for i in range(t):
	line1 = input().split(',')
	line2 = input().split(',')
	line3 = input().split()
	line4 = input().split()
	# after manipulations
	probs = [float(l) for l in line1]
	num_ladder = int(line2[0])
	num_snakes = int(line2[1])
	ladder = [l.split(',') for l in line3]
	ladder = {int(l[0]) : int(l[1]) for l in ladder}
	snakes = [l.split(',') for l in line4]
	snakes = {int(s[0]): int(s[1]) for s in snakes}
	ans.append(compute_expected_rolls())

for a in ans:
	print (round(a))