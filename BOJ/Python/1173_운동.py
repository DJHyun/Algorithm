# baekjoon source = "https://www.acmicpc.net/problem/1173"

import sys

n, m, M, T, R = map(int, sys.stdin.readline().split())

x = m
index = 0
time = 0
if x + T > M:
    print(-1)
else:
    while index < n:
        if x + T <= M:
            index += 1
            x += T
        else:
            x -= R
            if x < m:
                x = m
        time += 1

    print(time)
