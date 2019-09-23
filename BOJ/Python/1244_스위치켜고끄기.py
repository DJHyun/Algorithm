# baekjoon source = "https://www.acmicpc.net/problem/1244"

import sys


def change(a):
    if switch[a] == 1:
        switch[a] = 0
    else:
        switch[a] = 1

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
switch.insert(0, 0)
gen = int(sys.stdin.readline())

for i in range(gen):
    x, y = list(map(int, sys.stdin.readline().split()))

    if x == 1:
        for j in range(1, N + 1):
            if y * j <= N:
                change(j * y)
            else:
                break
    else:
        change(y)
        for j in range(1, N + 1):
            if (y - j) >= 1 and (y + j) <= N:
                if switch[y - j] == switch[y + j]:
                    change(y - j)
                    change(y + j)
                else:
                    break

for i in range(1, len(switch)):
    if i % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')
