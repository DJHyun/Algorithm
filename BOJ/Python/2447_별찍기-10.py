# baekjoon source = "https://www.acmicpc.net/problem/2447"
import sys

N = int(sys.stdin.readline())
result = [[' '] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i % 3 == 1 and j % 3 == 1:
            continue

        result[i][j] = '*'

        a,b = i,j
        while a > 0 and b > 0:
            if a%3 == 1 and b % 3 == 1:
                result[i][j] = ' '
            
            a //= 3
            b //= 3
        

for i in result:
    print(''.join(i))