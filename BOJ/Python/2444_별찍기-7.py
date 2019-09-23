# baekjoon source = "https://www.acmicpc.net/problem/2444"
import sys

N = int(sys.stdin.readline())
star = [[' ']*(N*2-1) for _ in range(N*2-1)]

for i in range(N*2-1):
    if i < N:
        for j in range(N-i-1,N+i):
            star[i][j] = '*'
    
    if i >= N:
        for j in range(i-N+1, (N*2-1)-(i-N+1)):
            star[i][j] = '*'

for i in star:
    print(''.join(i).rstrip())