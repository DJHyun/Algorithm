# baekjoon source = "https://www.acmicpc.net/problem/1026"

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b = sorted(b, reverse=True)
result = 0
for i in range(n):
    result += (a[i] * b[i])
print(result)
