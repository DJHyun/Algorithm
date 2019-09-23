# baekjoon source = "https://www.acmicpc.net/problem/11047"

import sys

N, K = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.reverse()
cnt = 0
for i in range(N):
    if arr[i] <= K:
        num = 0
        num += K//arr[i]
        K -= num*arr[i]
        cnt += num

    if K == 0:
        break

print(cnt)

