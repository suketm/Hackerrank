
ls_prime = [3,5,7] #prime numbers less than 125

def form_prime_ls():

    i = 11
    while i < 500:
        j = 3
        while j*j < i and i%j != 0:
            j += 2
        if i%j != 0:
            ls_prime.append(i)
        i += 2

form_prime_ls()

def find_power(number, prime_number):
    p = 0
    while number%prime_number == 0:
        p += 1
        number /= prime_number
    return p


def find_hcf(a, b):

    if a == 0:
        return b

    if b == 0:
        return a

    if a == b:
        return a

    if a > b:
        return find_hcf(a-b,b)

    return find_hcf(a, b-a)


def func(num):
    power_two = 0
    
    power_two = find_power(num,2)

    if power_two < 2:
        return (0)
    
    else:
        num /= 2**power_two
        odd_pow = 0
        if power_two % 2 != 0:
            odd_pow = 1

        i = 0
        power_ls = []
        total_prime = len(ls_prime)
        while num > 1 and i < total_prime:
            power = find_power(num, ls_prime[i])
            num /= ls_prime[i]**power
            if power != 0:
                if power % 2 != 0:
                    odd_pow = 1
                power_ls.append(power)
            i += 1

        if num != 1:
            power_ls.append(1)
            odd_pow = 1

        ans = [0,0]
        ans[0] = power_two//2
        ans[1] = power_two + 1

        for power in power_ls:
            ans[0] *= (power//2 + 1)
            ans[1] *= (power + 1)

        ans[1] -= 1
        if odd_pow == 0:
            ans[0] -= 1

        hcf = find_hcf(ans[0], ans[1])

        return str(int(ans[0]/hcf))+'/'+str(int(ans[1]/hcf))


t = int(input())

sol = []

for i in range(t):
    num = int(input())
    sol.append(func(num))


for i in range(t):
    print (sol[i])
