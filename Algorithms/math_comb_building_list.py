ls_string = []

t = int(input())

for i in range(t):
    _ = input()
    temp_string = input()
    ls_string.append(sorted(temp_string))



def func(temp_string, string, idx, n):

    for j in range(idx+1, n):

        temp_string_3 = string + temp_string[j]

        print (temp_string_3)

        func(temp_string, temp_string_3, j, n)


for temp_string in ls_string:
    n = len(temp_string)
    for i in range(n):
        temp_string_2 = temp_string[i]
        print (temp_string_2)
        func(temp_string, temp_string_2, i, n)
