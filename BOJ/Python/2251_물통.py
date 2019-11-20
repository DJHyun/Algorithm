# baekjoon source = "https://www.acmicpc.net/problem/2251"

import sys
from collections import deque

def solution(h):
    q = deque([h])
    visited.append(h)
    while q:
        t = q.popleft()
        for i in range(3):
            if t[i]:
                for j in range(3):
                    new_t = t[:]
                    if i == j:
                        continue
                    if m[j] - new_t[j] < new_t[i]:
                        score = m[j] - new_t[j]
                        new_t[j] += score
                        new_t[i] -= score
                    else:
                        new_t[j] += new_t[i]
                        new_t[i] = 0
                    if new_t not in visited:
                        if new_t[0] == 0:
                            result.append(new_t[2])
                        q.append(new_t)
                        visited.append(new_t)

a, b, c = map(int, sys.stdin.readline().split())
m = [a, b, c]
h = [0, 0, c]
result = deque()
visited = deque()

solution(h)
result = set(result)
result.add(c)
result = list(result)
result.sort()
print(*result)
