# baekjoon source = "https://www.acmicpc.net/problem/7569"
import sys
from collections import deque

def check(x, y, z):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if z < 0 or z > h - 1: return False
    if arr[z][x][y]: return False
    return True

def solution(x):
    global count

    q = deque(x)
    day = 0
    while q:
        len_ = len(q)
        for _ in range(len_):
            t = q.popleft()
            for i in range(4):
                tx = t[1] + dx[i]
                ty = t[2] + dy[i]
                if check(tx, ty,t[0]):
                    q.append([t[0], tx, ty])
                    arr[t[0]][tx][ty] = 1
                    count -= 1

            for i in range(2):
                tz = t[0] + dz[i]
                if check(t[1],t[2],tz):
                    q.append([tz,t[1],t[2]])
                    arr[tz][t[1]][t[2]] = 1
                    count -= 1

        if len(q):
            day += 1

    return day

m, n, h = map(int, sys.stdin.readline().split())
arr = [[[0] * m for _ in range(n)] for _ in range(h)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
dz = [1, -1]
count = 0
go = []

for i in range(h):
    for j in range(n):
        to = list(map(int, sys.stdin.readline().split()))
        for a in range(m):
            if to[a] == 0:
                count += 1
            elif to[a] == 1:
                go.append([i, j, a])
            arr[i][j][a] = to[a]

result = solution(go)

if count == 0:
    print(result)
else:
    print(-1)
