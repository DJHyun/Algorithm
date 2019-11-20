# baekjoon source = "https://www.acmicpc.net/problem/9372"

import sys

def find(x):
    if mst[x] == x:
        return x
    return find(mst[x])

def union(x, y):
    a = find(x)
    b = find(y)

    if a == b:
        return

    mst[a] = b

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    mst = [i for i in range(n + 1)]

    for i in range(m):
        union(arr[i][0], arr[i][1])

    che = find(1)
    cnt = 1
    for i in range(2, n + 1):
        if find(i) != che:
            cnt += 1
    print(n - cnt)


