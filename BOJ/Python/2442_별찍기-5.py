# baekjoon source = "https://www.acmicpc.net/problem/2442"
import sys

N = int(sys.stdin.readline())
arr = [[' ']*(N*2-1) for _ in range(N)]

for i in range(N-1,-1,-1):
    for j in range(i*2+(N-i-1),N-i-2,-1):
        arr[i][j] = '*'

for i in arr:
    print(''.join(i).rstrip())
