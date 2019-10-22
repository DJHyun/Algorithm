# baekjoon source = "https://www.acmicpc.net/problem/4963"

import sys
from collections import deque

def check(x, y):
    if x < 0 or x > h - 1: return False
    if y < 0 or y > w - 1: return False
    if visited[x][y]: return False
    return True

def bfs(x, y):
    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(8):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and arr[tx][ty] == 1:
                visited[tx][ty] = 1
                q.append([tx, ty])

dx, dy = [0, 0, 1, -1, 1, 1, -1, -1], [-1, 1, 0, 0, 1, -1, 1, -1]
while True:
    w, h = map(int, sys.stdin.readline().split())
    result = 0
    if w == 0 and h == 0:
        break

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j)
                result += 1

    print(result)
