import sys

sys.stdin = open('input (24).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    result = 0

    if a > b:
        for i in range(a - b + 1):
            re = 0
            for j in range(i, i + b):
                re += (arr_a[j] * arr_b[j-i])
            result = max(result, re)
    elif a < b:
        for i in range(b - a + 1):
            re = 0
            for j in range(i, i + a):
                re += (arr_a[j-i] * arr_b[j])
            result = max(result, re)
    else:
        re = 0
        for j in range(a):
            re += (arr_a[j] * arr_b[j])
        result = max(result, re)

    print(f'#{test_case} {result}')
