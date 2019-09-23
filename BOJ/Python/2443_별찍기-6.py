# baekjoon source = "https://www.acmicpc.net/problem/2443"
import sys

N = int(sys.stdin.readline())
star = [[' ']*(2*N-1) for _ in range(N)]

for i in range(N):
    for j in range(i,2*N-i-1):
        star[i][j] = '*'

for i in star:
    print(''.join(i).rstrip())