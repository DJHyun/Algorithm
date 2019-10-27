# baekjoon source = "https://www.acmicpc.net/problem/2206"

import sys
from collections import deque

def check(x, y, z, c):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if visited[x][y][z]: return False
    if c == 1:
        if arr[x][y] == 1:
            return False
    return True

def solution(x, y):
    q = deque([[x, y, 0, 1]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            tz = t[2]
            if check(tx, ty, tz, tz):
                if arr[tx][ty] == 1:
                    if tz == 0:
                        q.append([tx, ty, tz + 1,t[3]+1])
                        visited[tx][ty][tz + 1] = 1
                        if tx == n - 1 and ty == m - 1:
                            return t[3] + 1
                else:
                    q.append([tx, ty, tz,t[3]+1])
                    visited[tx][ty][tz] = 1
                    if tx == n - 1 and ty == m - 1:
                        return t[3] + 1
    return -1

n, m = map(int, sys.stdin.readline().split())
if n == 1 and m == 1:
    print(1)
else:
    arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    visited = [[[0, 0] for _ in range(m)] for i in range(n)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    visited[0][0][0] = 1
    visited[0][0][1] = 1

    print(solution(0, 0))
