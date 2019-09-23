import sys

sys.stdin = open("4008_숫자만들기.txt", "r")

def solution(x, sum_):
    global n, max_result, min_result, cnt, gogo

    # print(x, sum_, n-1)
    if x == n - 1:
        cnt += 1
        max_result = max(max_result, sum_)
        min_result = min(min_result, sum_)
        return 0

    for i in range(4):
        if gogo[i] != 0:
            if i == 0:
                gogo[i] -= 1
                solution(x + 1, sum_ + numbers[x + 1])
                gogo[i] += 1
            elif i == 1:
                gogo[i] -= 1
                solution(x + 1, sum_ - numbers[x + 1])
                gogo[i] += 1
            elif i == 2:
                gogo[i] -= 1
                solution(x + 1, sum_ * numbers[x + 1])
                gogo[i] += 1
            elif i == 3:
                gogo[i] -= 1
                solution(x + 1, int(sum_ / numbers[x + 1]))
                gogo[i] += 1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    check = list(map(int, input().split()))
    cnt = 0
    max_result = -100000001
    min_result = 100000001
    gogo = check[:]

    visited = [0] * (n - 1)
    numbers = list(map(int, input().split()))
    solution(0, numbers[0])

    print(f'#{test_case} {max_result - min_result}')