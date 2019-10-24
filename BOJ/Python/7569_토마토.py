# baekjoon source = "https://www.acmicpc.net/problem/7569"
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if visited[x][y]: return False
    if arr[x][y] == -1: return False
    return True

def solution(x, y):
    global count

    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(6):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                q.append([tx, ty])
                visited[tx][ty] = 1
                if arr[tx][ty] == 0:
                    count -= 1

m, n, h = map(int, sys.stdin.readline().split())
arr = [[0] * m for _ in range(n * h)]
visited = [[0] * m for _ in range(n * h)]
dx, dy = [0, 0, 1, -1, n, -n], [1, -1, 0, 0, 0, 0]
count = 0

for i in range(n * h):
    to = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if to[j] == 0:
            count += 1
        arr[i][j] = to[j]

result = 0
for i in range(n * h):
    for j in range(m):
        if arr[i][j] == 1:
            visited[i][j] = 1
            solution(i, j)

print(count)
for i in arr:
    print(i)
