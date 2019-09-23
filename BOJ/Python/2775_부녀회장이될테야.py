# baekjoon source = "https://www.acmicpc.net/problem/2775"

import sys

T = int(sys.stdin.readline())
apt = [[0]*14 for _ in range(15)]
apt[0] = list(range(1,15))

for i in range(15):
    apt[i][0] = 1

for _ in range(T):
    k, n = int(sys.stdin.readline()),int(sys.stdin.readline())

    if n == 1:
        print(1)
        continue

    for i in range(1,k+1):
        for j in range(1,n):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]

    print(apt[i][j])

