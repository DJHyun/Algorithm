# baekjoon source = "https://www.acmicpc.net/problem/2468"
import sys
from collections import deque

def error(x, y, v):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] <= v: return False
    return True

def solution(x, y, v):
    que = deque([[x, y]])
    visited[x][y] = index

    while que:
        t = que.popleft()
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if error(x, y, v) and index > visited[x][y]:
                que.append([x, y])
                visited[x][y] = index

n = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]
check = set()
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        arr[i][j] = num[j]
        check.add(num[j])

result = 1
index = 0
while check:
    index += 1
    c = check.pop()
    count = 0
    for i in range(n):
        for j in range(n):

            if arr[i][j] > c and index > visited[i][j]:
                solution(i, j, c)
                count += 1

    result = max(result, count)

print(result)
