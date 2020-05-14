
n = int(input())
arr = [int(element) for element in input().split()]

dict_num_freq = {a:arr.count(a) for a in set(arr)}

freq = max(dict_num_freq.values())

print (min([k for k,v in dict_num_freq.items() if v == freq]))