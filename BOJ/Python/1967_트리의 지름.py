# baekjoon source = "https://www.acmicpc.net/problem/1967"

import sys
from collections import deque

def solution(x):
    global result
    q = deque([[x, 0]])
    visited[x] = 1
    while q:
        t = q.popleft()
        flag = True
        for i in range(len(arr[t[0]])):
            c = arr[t[0]][i]
            if not visited[c[0]]:
                q.append([c[0], t[1] + c[1]])
                visited[c[0]] = 1
                flag = False

        if flag:
            result = max(result, t[1])

n = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
check = [[] for _ in range(n+1)]
mx = 0
result = 0

for i in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    solution(i)
    check[i].append(result)

print(result)
