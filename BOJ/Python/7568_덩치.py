# baekjoon source = "https://www.acmicpc.net/problem/7568"

import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            result[i] += 1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            result[j] += 1

print(*result)