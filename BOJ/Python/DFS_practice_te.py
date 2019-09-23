import sys

T = list(map(int,sys.stdin.readline().split(',')))

number,visited,stack,result = [[] for i in range(max(T)+1)],[0]*(max(T)+1),[0]*max(T),[]
top = -1

for i in range(len(T)):
    if not i%2:
        number[T[i]].append(T[i+1])
        number[T[i+1]].append(T[i])

def dfs_teacher(v):
    print(v)
    visited[v] = True
    
    for i in range(1,8):
        if number[v][i] and not visited[i]:
            dfs_teacher(v)

print(number)
print(dfs_teacher(1))