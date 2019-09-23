# baekjoon source = "https://www.acmicpc.net/problem/2798"

import sys

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

min_ = M
flag = True
for i in range(N):
    if flag:
        for j in range(i + 1, N):
            if flag:
                for z in range(j + 1, N):
                    if a[i] + a[j] + a[z] <= M:
                        min_ = min(min_, abs(a[i] + a[j] + a[z] - M))
                    if min_ == 0:
                        flag = False
                        break
print(M - min_)
