# baekjoon source = "https://www.acmicpc.net/problem/10163"

import sys

N = int(sys.stdin.readline())

arr = [[0] * 101 for _ in range(101)]
result = [0] * (N + 1)

for i in range(N):
    a, b, x, y = map(int, sys.stdin.readline().split())

    for j in range(x):
        for z in range(y):
            arr[a + j][b + z] = (i + 1)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        result[arr[i][j]] += 1

result.pop(0)
for i in result:
    print(i)
