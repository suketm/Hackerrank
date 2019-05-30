
import sys
sys.setrecursionlimit(120000)

n, p = map(int, input().split())


graph = {i:set() for i in range(n)}

for i in range(p):
    x1, x2 = map(int, input().split())
    graph[x1].add(x2)
    graph[x2].add(x1)


ls = []
status = [0]*n

def dfs(temp_ver):
    global val
    val += 1
    status[temp_ver] = 1
    for new_ver in graph[temp_ver]:
        if status[new_ver] == 0:
            dfs(new_ver)

for vertex in graph:
    if status[vertex] == 0:
        val = 0
        dfs(vertex)
        ls.append(val)



n2 = len(ls)

if n2 == 1:
    ans = 0

elif n2 >= 2:
    ans = ls[0]*ls[1]
    temp_ans = ls[0]+ls[1]
    for i in range(2,n2):
        ans += temp_ans*ls[i]
        temp_ans += ls[i]
    
print (ans)
