# baekjoon source = "https://www.acmicpc.net/problem/11724"

import sys
from collections import deque

def solution(x):
    q = deque([x])
    visited[x] = 1
    while q:
        t = q.popleft()
        for i in range(1, n + 1):
            if arr[t][i] == 1 and not visited[i]:
                visited[i] = 1
                q.append(i)

n, m = map(int, sys.stdin.readline().split())
input_ = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in input_:
    arr[i[0]][i[1]] = 1
    arr[i[1]][i[0]] = 1

result = 0
for i in range(1,n+1):
    if not visited[i]:
        solution(i)
        result += 1
print(result)
