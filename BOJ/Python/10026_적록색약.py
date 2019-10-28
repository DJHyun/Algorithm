# baekjoon source = "https://www.acmicpc.net/problem/10026"

import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if visited[x][y]: return False
    return True

def solution(x, y, a):
    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                if a == 0:
                    if arr[x][y] == arr[tx][ty]:
                        q.append([tx, ty])
                        visited[tx][ty] = 1
                else:
                    if arr[x][y] == 'R' or arr[x][y] == 'G':
                        if arr[tx][ty] == 'R' or arr[tx][ty] == 'G':
                            q.append([tx,ty])
                            visited[tx][ty] = 1
                    else:
                        if arr[x][y] == arr[tx][ty]:
                            q.append([tx, ty])
                            visited[tx][ty] = 1

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

count = [0, 0]
for a in range(2):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                solution(i, j, a)
                count[a] += 1

print(*count)
