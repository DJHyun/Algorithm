# baekjoon source = "https://www.acmicpc.net/problem/10814"

import sys
from collections import deque
n = int(sys.stdin.readline())
result = deque()
for i in range(n):
    a, b = sys.stdin.readline().split()
    result.append([i + 1, int(a), b])
result = sorted(result, key=lambda x: (x[1], x[1]))
for i in result:
    print(*i[1:])