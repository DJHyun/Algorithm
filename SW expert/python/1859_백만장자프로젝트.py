import sys

sys.stdin = open("1859_백만장자프로젝트.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    count = 0
    max_ = max(price)
    buy = 0
    result = 0

    for i in range(n):
        if price[i] < max_:
            count += 1
            buy += price[i]

        elif price[i] >= max_:
            result += ((price[i] * count)-buy)
            count = 0
            buy = 0
            if i != (n - 1):
                max_ = max(price[i + 1:])

    print(f'#{test_case} {result-buy}')
