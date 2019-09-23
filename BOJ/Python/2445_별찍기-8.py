# baekjoon source = "https://www.acmicpc.net/problem/2445"
import sys

N = int(sys.stdin.readline())
star = [['*']*(2*N) for _ in range(2*N-1)]

for i in range(2*N-1):
    if i < N:
        for j in range(i+1, 2*N-1-i):
            star[i][j] = ' '

    if i >= N:
        for j in range(2*N-1-i,i+1):
            star[i][j] = ' '

for i in star:
    print(''.join(i).rstrip())