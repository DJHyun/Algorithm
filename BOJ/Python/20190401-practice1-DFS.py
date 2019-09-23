def dfs(x):
    visited[x] = True
    if x != 1:
        print('-', end='')
        print(x, end='')
    else:
        print(x, end=''
              )
    if x == max(v):
        return

    for i in range(len(arr[x])):
        if not visited[arr[x][i]]:
            # print(x)
            dfs(arr[x][i])

v = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
arr = [[] for _ in range(max(v) + 1)]
visited = [0] * (max(v) + 1)
for i in range(0, len(v), 2):
    arr[v[i]].append(v[i + 1])
    arr[v[i + 1]].append(v[i])

# brr = [[0]*(max(v)+1) ]

for i in arr:
    print(i)

dfs(1)
