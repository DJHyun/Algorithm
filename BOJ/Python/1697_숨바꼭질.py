# baekjoon source = "https://www.acmicpc.net/problem/1697"

import sys
from collections import deque

def solution(a, b, depth):
    q = deque([[a, depth]])
    while q:
        wq = len(q)
        for i in range(wq):
            t = q.popleft()
            if t[0] < 0:
                continue
            if t[0]+1 < 100001 and not visited[t[0] + 1] :
                if t[0] + 1 == b:
                    return t[1] + 1
                visited[t[0]+1] = 1
                q.append([t[0] + 1, t[1] + 1])
            if not visited[t[0] - 1] and t[0] > 0:
                if t[0] - 1 == b:
                    return t[1] + 1
                visited[t[0]-1] =1
                q.append([t[0] - 1, t[1] + 1])
            if t[0]*2 < 100001 and not visited[t[0] * 2] :
                if t[0] * 2 == b:
                    return t[1] + 1
                visited[t[0]*2] =1
                q.append([t[0] * 2, t[1] + 1])

a, b = map(int, sys.stdin.readline().split())
visited = [0] * 100001
if a == b:
    print(0)
else:
    visited[a] = 1
    print(solution(a, b, 0))
