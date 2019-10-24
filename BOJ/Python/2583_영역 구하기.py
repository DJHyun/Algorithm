# baekjoon source = "https://www.acmicpc.net/problem/2583"

import sys
from collections import deque

def check(x, y):
    if x < 0 or x > m - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] == 1: return False
    return True

def solution(x, y):
    q = deque([[x, y]])
    score = 1
    arr[x][y] = 1
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                arr[tx][ty] = 1
                score += 1
                q.append([tx, ty])

    return score

m, n, k = map(int, sys.stdin.readline().split())
arr = [[0] * n for _ in range(m)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(k):
    b, a, d, c = map(int, sys.stdin.readline().split())
    for x in range(a, c):
        for y in range(b, d):
            arr[x][y] = 1

count = 0
result = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            result.append(solution(i, j))
            count += 1

print(count)
result.sort()
print(' '.join(map(str,result)))
