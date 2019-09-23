import sys
sys.stdin = open("회전.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    number = list(map(int,input().split()))
    [number.append(number.pop(0)) for _ in range(M)]
    print(f'#{test_case} {number[0]}')
