# baekjoon source = "https://www.acmicpc.net/problem/9517"

import sys

bomb = 210
k = int(sys.stdin.readline())
if k == 0:
    k = 7
else:
    k -= 1
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(n)]

time = 0
for i in arr:

    if i[1] == 'T':
        time += int(i[0])
        if time >= bomb:
            print(k+1)
            break
        k += 1
        k %= 8
    else:
        time += int(i[0])
        if time >= bomb:
            print(k+1)
            break

