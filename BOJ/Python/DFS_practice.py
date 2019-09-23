# 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7

import sys

T = list(map(int,sys.stdin.readline().split(',')))

number,visited,stack,result = [[] for i in range(max(T)+1)],[0]*(max(T)+1),[0]*max(T),[]
top = -1

for i in range(len(T)):
    if not i%2:
        number[T[i]].append(T[i+1])
        number[T[i+1]].append(T[i])

def dfs(n):
    visited.append(n)
    global top 
    top += 1
    stack[top] = n

    while(top != -1):
        while(n != -1):
            for i in number[n]:
                if i not in visited:
                    visited.append(i)
                    top += 1
                    stack[top] = i
                    n = i
                    break
            else:
                n = -1
        n = stack.pop(top)
        top -= 1
    return visited

def dfs_teacher(v):
    print(v)
    visited[v] = True
    print(visited)
    for i in range(1,8):
        if number[v][i] and not visited[i]:
            dfs_teacher(v)

print(number)
print(dfs_teacher(1))