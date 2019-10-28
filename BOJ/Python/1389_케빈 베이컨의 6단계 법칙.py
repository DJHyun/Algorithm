# baekjoon source = "https://www.acmicpc.net/problem/1389"

import sys
from collections import deque

def solution(x):
    q = deque([[x, 0]])
    while q:
        t = q.popleft()
        for i in range(1, n + 1):
            if arr[t[0]][i] == 1 and not visited[i]:
                q.append([i, t[1] + 1])
                visited[i] = t[1] + 1

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

result = float('inf')
val = 0
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    visited[i] = 1
    solution(i)
    r = sum(visited) - 1
    if result > r:
        result = r
        val = i

print(val)
