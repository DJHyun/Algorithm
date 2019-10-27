# baekjoon source = "https://www.acmicpc.net/problem/2589"
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == 'W': return False
    return True

def solution(x, y):
    global result,count

    q = deque([[x,y]])
    visited[x][y] = 1
    cnt = 0

    while q:
        len_ = len(q)
        cnt += 1
        for le in range(len_):
            t = q.popleft()
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x, y) and count > visited[x][y]:
                    q.append([x, y])
                    visited[x][y] = count

    result = max(result, cnt-1)

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
result = 0
count = 0

for i in range(n):
    for j in range(m):
        count += 1
        if arr[i][j] == 'L':
            solution(i, j)

print(result)