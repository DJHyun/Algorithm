# baekjoon source = "https://www.acmicpc.net/problem/2146"

import sys
from collections import deque

def check(x, y, index):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if visited[x][y]: return False
    if not arr[x][y]:
        if visited[x][y] != -1:
            go.append([x, y,index])
            visited[x][y] = -1
        return False
    return True

def sol_check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def label(x, y, index):
    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty, index) and not visited[tx][ty]:
                q.append([tx, ty])
                arr[tx][ty] = index
                visited[tx][ty] = 1

def solution(x, y,id):
    global result

    q = deque([[x, y, 0]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if sol_check(tx, ty) and not visited[tx][ty]:
                if result <= t[2]+1:
                    continue
                if not arr[tx][ty]:
                    visited[tx][ty] = 1
                    q.append([tx,ty,t[2]+1])
                elif arr[tx][ty] != id:
                    result = min(result,t[2]+1)


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0] * n for _ in range(n)]
index = 1
go = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = 1
            arr[i][j] = index
            label(i, j, index)
            index += 1
result = float('inf')
for i in go:
    visited = [[0] * n for _ in range(n)]
    solution(i[0], i[1],i[2])

print(result)