# SW Expert Academy

import sys

sys.stdin = open('input.txt', 'r')

def solution(a):
    x = a // 100
    y = a % 100
    arr[x][y] = 3

    if x == 0:
        print(f'#{tc} {y}')
        return

    if y < 99 and arr[x][y + 1] == 1:
        solution(x * 100 + y + 1)
    elif y > 0 and arr[x][y - 1] == 1:
        solution(x * 100 + y - 1)
    else:
        solution((x - 1) * 100 + y)

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().strip().split(" "))) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            solution(99 * 100 + i)
            break
