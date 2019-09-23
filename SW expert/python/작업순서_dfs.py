def dfs(v):
    global top
    global idx

    if not visited[v]:
        top += 1
        stack[top] = v

    visited[v] = True

    for i in range(1,len(G)):
        if G[v][i] and not visited[i]:
            dfs(i)

    if v not in result:
        result[idx] = v
        idx += 1

for test_case in range(1, 11):
    v, e= list(map(int,input().split()))
    g = list(map(int,input().split()))[::-1]
    G = [[0]*(v+1) for _ in range(v+1)]
    visited, stack = [0]*(v+1),[0]*(v+1)
    idx = 0
    result = [0]*v
    top = -1

    for a in range(0,len(g),2):
        G[g[a]][g[a+1]] = 1

    for i in range(1,len(G)):
        if i and not visited[i]:
            dfs(i)
    
    print(f'#{test_case} {" ".join(list(map(str,result))).strip()}')