# baekjoon source = "https://www.acmicpc.net/problem/17142"
from itertools import combinations

def check(x, y):
    global visited

    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] == 1: return False
    if visited[x][y]: return False
    return True

def solution(a):
    global cnt

    tq = []
    count = 0
    c = 1
    result = 0
    for i in range(m):
        tq.append(a[i])
        visited[a[i][0]][a[i][1]] = -1

    while tq and count < cnt:
        q = tq[:]
        tq.clear()
        while q:
            t = q.pop(0)
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x,y):
                    visited[x][y] = c
                    if arr[x][y] == 0:
                        count += 1
                    tq.append([x, y])

        c += 1
        result += 1

    if count == cnt:
        return result
    else:
        return 99999999



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
r = 999999999

bi = []
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            bi.append([i, j])
        if arr[i][j] == 0:
            cnt += 1

im = combinations(bi, m)

for i in im:
    visited = [[0] * n for _ in range(n)]
    r = min(r,solution(i))

if r == 99999999:
    print(-1)
else:
    print(r)

