# baekjoon source = "https://www.acmicpc.net/problem/2468"

import sys
from collections import deque

def check(x, y, z):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] <= z: return False
    return True

def solution(x, y, z):
    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty, z) and not visited[tx][ty]:
                visited[tx][ty] = 1
                q.append([tx, ty])

n = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]
max_ = 0
check_list = [0] * 101
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(n):
    go = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        max_ = max(max_, go[j])
        check_list[go[j]] = 1
        arr[i][j] = go[j]

result = 1
for i in range(max_ + 1):
    visited = [[0] * n for _ in range(n)]
    count = 0
    if check_list[i]:
        for a in range(n):
            for b in range(n):
                if arr[a][b] > i and not visited[a][b]:
                    visited[a][b] = 1
                    solution(a, b, i)
                    count += 1
    result = max(result, count)

print(result)
