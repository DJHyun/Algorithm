# baekjoon source = "https://www.acmicpc.net/problem/17845"
'''
110 3
650 40
700 60
60 40
'''
import sys

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
memo = [[0] * k for _ in range(k)]
result = 0
for i in arr:
    print(i)
print()
for i in memo:
    print(i)
print()
for i in range(k):
    for j in range(k):
        if i == j:
            continue

        elif arr[i][1] + arr[j][1] <= n:
            memo[i][j] = arr[i][0] + arr[j][0]

for i in memo:
    print(i)
print(result)
