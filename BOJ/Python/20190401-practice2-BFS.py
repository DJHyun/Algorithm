def bfs(x):
    q = []
    q.append(x)
    visited.append(x)
    while q:
        t = q.pop(0)
        if t == 1:
            print(t,end='')
        else:
            print('-',end='')
            print(t,end='')
        for i in range(len(arr[t])):
            if arr[t][i] not in visited:
                q.append(arr[t][i])
                visited.append(arr[t][i])


v = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
arr = [[] for _ in range(max(v) + 1)]
visited = [0]*max(v)
for i in range(0,len(v),2):
    arr[v[i]].append(v[i+1])
    arr[v[i+1]].append(v[i])

for i in arr:
    print(i)

bfs(1)
