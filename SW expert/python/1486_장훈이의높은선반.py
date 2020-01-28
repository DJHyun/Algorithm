# SW Expert Academy
import sys

sys.stdin = open("1486_장훈이의높은선반.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    result = 9999999999

    for i in range(1, (1 << N)):
        total = []
        for j in range(N):
            if i & (1 << j):
                total.append(height[j])
        if sum(total) >= B:
            result = min(result, sum(total)-B)

    print(f'#{test_case} {result}')
