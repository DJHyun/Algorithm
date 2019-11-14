# baekjoon source = "https://www.acmicpc.net/problem/2161"

import sys
from collections import deque

i = int(sys.stdin.readline())
q = deque(list(range(1,i+1)))

while len(q) != 1:
    sys.stdout.write(str(q.popleft())+" ")
    q.append(q.popleft())

print(q[0])