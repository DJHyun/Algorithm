import sys

sys.stdin = open('input (21).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    x, y = 0, 0

    if a + c >= 13:
        x = a + c - 12
    else:
        x = a + c

    if b + d > 59:
        x += 1
        if x >= 13:
            x -= 12
        y = b + d - 60
    else:
        y = b + d

    print(f'#{test_case} {x} {y}')
