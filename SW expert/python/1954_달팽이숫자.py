# SWEA source = "SW Expert Academy 1954_달팽이숫자"
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    x, y, cnt, d = 0, 0, 1, 0
    arr[x][y] = cnt

    print(f'#{test_case}')
    if n == 1:
        print(1)
        continue

    while cnt < n * n:
        cnt += 1

        if d == 0:
            y += 1
            if y > n - 1 or arr[x][y] != 0:
                d = 1
                y -= 1
                cnt -= 1
        elif d == 1:
            x += 1
            if x > n - 1 or arr[x][y] != 0:
                d = 2
                x -= 1
                cnt -= 1
        elif d == 2:
            y -= 1
            if y < 0 or arr[x][y] != 0:
                d = 3
                y += 1
                cnt -= 1
        else:
            x -= 1
            if x < 0 or arr[x][y] != 0:
                d = 0
                x += 1
                cnt -= 1

        arr[x][y] = cnt

    for i in arr:
        print(' '.join(map(str, i)))
