# baekjoon source = "https://www.acmicpc.net/problem/8320"

import sys

n = int(sys.stdin.readline())
idx = 0
cnt = 1

while cnt != n+1:
    o = 0
    for i in range(1,cnt+1):
        if cnt % i == 0:
            o += 1
    idx += ((o+1)//2)
    cnt += 1
print(idx)
