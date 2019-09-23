import sys

sys.stdin = open('1493_수의새로운연산.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b = list(map(int, input().split()))
    flag = True
    c = d = 0

    result = (0,0)
    idx = 1
    x = 1
    y = 1
    k = 1
    while True:

        if idx == a:
            c = (x, y)

        if idx == b:
            d = (x, y)

        idx += 1

        if c != 0 and d != 0:
            result = (c[0]+d[0],c[1]+d[1])

        if result[0] == x and result[1] == y:
            print(f'#{test_case} {idx-1}')
            break

        if y == 1:
            x = 1
            y = k + 1
            k += 1
        else:
            x += 1
            y -= 1