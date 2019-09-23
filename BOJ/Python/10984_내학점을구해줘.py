# baekjoon source = "https://www.acmicpc.net/problem/12790"

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    score, avg = 0, 0
    for i in range(N):
        num = list(map(float,sys.stdin.readline().split()))
        score += num[0]
        avg += num[0] * num[1]

    print("%0.0f" % score, "%0.1f" % (avg/score))