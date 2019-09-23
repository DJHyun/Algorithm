import sys

sys.stdin = open("1952_수영장.txt", "r")

def solution(x, sum_, check):
    global result

    if result <= sum_:
        return 1

    if x == 12:
        result = min(sum_,result)
        return 1

    for i in range(3):
        if days[x] == 0:
            if check != 0:
                solution(x + 1, sum_, check - 1)
            else:
                solution(x + 1, sum_, check)
        elif check != 0:
            solution(x + 1, sum_, check - 1)
        elif i == 0:
            solution(x + 1, sum_ + (prices[0] * days[x]), 0)
        elif i == 1:
            solution(x + 1, sum_ + prices[1], 0)
        else:
            solution(x + 1, sum_ + prices[2], 2)


T = int(input())
for test_case in range(1, T + 1):
    prices = list(map(int, input().split()))
    days = list(map(int, input().split()))
    result = 999999999

    solution(0,0,0)

    print(f'#{test_case} {min(prices[3], result)}')
