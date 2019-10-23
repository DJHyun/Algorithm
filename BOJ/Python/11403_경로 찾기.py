# baekjoon source = "https://www.acmicpc.net/problem/11403"
import sys
from collections import deque

def solution(x):
    global n

    q = deque([x])
    while q:
        t = q.popleft()
        for i in range(n):
            if arr[t][i] and not visited[i]:
                visited[i] = 1
                q.append(i)

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    visited = [0] * n
    solution(i)
    print(' '.join(map(str,visited)))
