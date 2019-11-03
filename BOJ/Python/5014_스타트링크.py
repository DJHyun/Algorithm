# baekjoon source = "https://www.acmicpc.net/problem/5014"
import sys
from collections import deque

def check(x):
    global f, u, d

    if x + u > f: return False
    if x - d < 1: return False
    if visited[x]: return False
    return True

def solution(x):
    q = deque([[x, 0]])
    visited[x] = 1
    while q:
        t = q.popleft()
        a, b = t[0] + u, t[0] - d
        if a == g or b == g:
            return t[1] + 1

        if check(a) and not visited[a]:
            q.append([a, t[1] + 1])
            visited[a] = 1

        if check(b) and not visited[b]:
            q.append([b, t[1] + 1])
            visited[b] = 1

f, s, g, u, d = map(int, sys.stdin.readline().split())
visited = [0] * (f + 1)

if s == g:
    print(0)
else:
    result = solution(s)
    if result == None:
        print('use the stairs')
    else:
        print(result)