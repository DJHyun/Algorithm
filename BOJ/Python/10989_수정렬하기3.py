# baekjoon source = "https://www.acmicpc.net/problem/10989"

import sys

T = int(sys.stdin.readline())
mlist = [0 for i in range(10001)]

for i in range(T):
    mlist[int(sys.stdin.readline())] += 1

for i,v in enumerate(mlist):
    if v != 0:
        for r in range(v):
            print(i)