
import sys
sys.stdin = open("min_max.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number = sorted(list(map(int,input().split())))
    print(f'#{test_case} {number[-1] - number[0]}')
