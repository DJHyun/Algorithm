# baekjoon source = "https://www.acmicpc.net/problem/17501"

import sys
from collections import deque


def solution(x):
    q = deque()
    q.append(arr[x])
    while q:
        t = q.popleft()




n = int(sys.stdin.readline())
visited = [0]*(n+1)
arr = [[] for _ in range(2*n)]
for i in range(1,2*n):
    if i <= n:
        arr[i] = [int(sys.stdin.readline())]
    else:
        arr[i] = sys.stdin.readline().split()

for i in arr:
    print(i)

visited[2*n-1] = 1
solution(2*n-1)