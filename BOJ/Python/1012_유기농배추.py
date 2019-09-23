# baekjoon source = "https://www.acmicpc.net/problem/1012"

import sys

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == 0: return False
    return True

def solution(a):
    q = [a]
    while q:
        t = q.pop(0)
        for i in range(4):
            x = t // 100 + dx[i]
            y = t % 100 + dy[i]
            if check(x,y):
                arr[x][y] = 0
                q.append(x*100+y)



T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0] * m for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = 0

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                solution(i*100+j)
                result += 1

    print(result)
