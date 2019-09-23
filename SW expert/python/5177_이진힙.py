import sys

sys.stdin = open("이진힙.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    arr = [[0] * 3 for _ in range(max(number) + 1)]
    result = [0] * (N + 1)

    for i in range(1, N + 1):
        if i == 1:
            result[i] = number[i - 1]
        else:
            if result[i // 2] > number[i - 1]:
                result[i // 2], result[i] = number[i - 1], result[i // 2]
                while i > 0:
                    i //= 2
                    if result[i // 2] > result[i]:
                        result[i // 2], result[i] = result[i], result[i // 2]
            else:
                result[i] = number[i - 1]

    cnt = 0
    while N >= 1:
        cnt += result[N//2]
        N //= 2

    print('#{} {}'.format(test_case,cnt))
