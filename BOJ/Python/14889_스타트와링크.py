# baekjoon source = "https://www.acmicpc.net/problem/14889"
import sys

def dfs(a, k, check):
    global min_
    c = [0] * N

    one, two = 0, 0
    if k == check:
        b = list(range(1,N+1))
        for i in range(1,N//2+1):
            b.pop(b.index(a[i]))

        for j in range(1,N // 2+1):
            for i in range(j + 1, N // 2+1):
                one += arr[a[j] - 1][a[i] - 1]
                one += arr[a[i] - 1][a[j] - 1]

        for j in range(N//2):
            for i in range(j + 1, N//2):
                two += arr[b[j] - 1][b[i] - 1]
                two += arr[b[i] - 1][b[j] - 1]

        min_ = min(min_, abs(one - two))
    else:
        k += 1
        candi = ncandi(a, k, N, c)
        for i in range(candi):
            a[k] = c[i]
            dfs(a, k, check)
            a[k] = 0
            if a[1] != 1:
                break

def ncandi(a, k, check, c):
    visited = [False] * (check + 1)

    max_ = max(a)
    for i in range(max_,-1,-1):
        visited[i] = True

    candi = 0
    for i in range(1, check + 1):
        if not visited[i]:
            c[candi] = i
            candi += 1

    return candi

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a = [0] * (N//2+1)
number = list(range(N))
result = []
min_ = 200000

dfs(a, 0, N//2)

print(min_)
