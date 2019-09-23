# baekjoon source = "https://www.acmicpc.net/problem/2669"

import sys
arr = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(4):

    x,y,a,b = map(int,sys.stdin.readline().split())

    for i in range(x,a):
        for j in range(y,b):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1

print(cnt)
