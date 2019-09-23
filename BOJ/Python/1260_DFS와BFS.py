# baekjoon source = "https://www.acmicpc.net/problem/1260"
'''
6 5 2
1 2
1 3
2 4
3 5
3 6
'''
import sys

def dfs(x):

    dfs_visited.append(x)
    print(x, end=' ')
    for i in range(1,N+1):
        if arr[x][i] == 1 and i not in dfs_visited:
            dfs(i)


def bfs(x):
    q = []
    bfs_visited = []
    q.append(x)
    bfs_visited.append(x)
    while q:
        t = q.pop(0)
        print(t, end= ' ')
        for i in range(1, N + 1):
            if arr[t][i] == 1 and i not in bfs_visited:
                q.append(i)
                bfs_visited.append(i)

N, M, V = map(int,sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]
dfs_visited = []



for i in range(M):
    num = list(map(int,sys.stdin.readline().split()))
    arr[num[0]][num[1]] = 1
    arr[num[1]][num[0]] = 1


for i in arr:
    print(i)

dfs(V)
print()
bfs(V)