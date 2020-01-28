# SW Expert Academy
import sys
sys.stdin = open('input (2).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    d = list(map(int,input().split()))
    result = 9999999
    cnt = 0
    for i in range(n):
        if result > abs(d[i]):
            result = abs(d[i])
            cnt = 1
        elif result == abs(d[i]):
            cnt += 1

    print(f'#{test_case} {result} {cnt}')