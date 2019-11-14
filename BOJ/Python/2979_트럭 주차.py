# baekjoon source = "https://www.acmicpc.net/problem/2979"

import sys

a, b, c = map(int, sys.stdin.readline().split())
arr = [[0, 0] for _ in range(3)]
max_ = 0
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    max_ = max(y, max_)
    arr[i][0] = x
    arr[i][1] = y

index = 0
result = 0
while index <= max_:
    count = 0
    for i in range(3):
        if arr[i][0] <= index < arr[i][1]:
            count += 1

    if count == 1:
        result += a
    elif count == 2:
        result += 2 * b
    elif count == 3:
        result += 3 * c

    index += 1
print(result)