# baekjoon source = "https://www.acmicpc.net/problem/11404"

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
result = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    result[arr[i][0]][arr[i][1]] = min(arr[i][2], result[arr[i][0]][arr[i][1]])

for i in range(1, n + 1):
    result[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if result[i][j] > result[i][k] + result[k][j]:
                result[i][j] = result[i][k] + result[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if result[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()
