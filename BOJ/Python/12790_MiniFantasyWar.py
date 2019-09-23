# baekjoon source = "https://www.acmicpc.net/problem/12790"

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    i = list(map(int, sys.stdin.readline().split()))
    a = 1 if i[0] + i[4] < 1 else i[0] + i[4]
    b = 1 if i[1] + i[5] < 1 else i[1] + i[5]
    c = 0 if i[2] + i[6] < 0 else i[2] + i[6]
    d = i[3] + i[7]
    print(a + b * 5 + c * 2 + d * 2)
