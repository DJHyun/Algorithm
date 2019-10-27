# baekjoon source = "https://www.acmicpc.net/problem/2644"

import sys
from collections import deque

def solution(x):
    q = deque([[x, 0]])
    while q:
        t = q.popleft()
        for i in range(1, n + 1):
            if arr[t[0]][i] == 1 and not visited[i]:
                if i == two:
                    return t[1] + 1
                q.append([i, t[1] + 1])
                visited[i] = 1

    return -1

n = int(sys.stdin.readline())
one, two = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

print(solution(one))