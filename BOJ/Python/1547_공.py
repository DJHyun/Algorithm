# baekjoon source = "https://www.acmicpc.net/problem/1547"

import sys

m = int(sys.stdin.readline())
result = {1: 1, 2: 2, 3: 3}

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    result[a], result[b] = result[b], result[a]

for i,v in result.items():
    if v == 1:
        print(i)
        break
