# baekjoon source = "https://www.acmicpc.net/problem/3048"

import sys

a, b = map(int, sys.stdin.readline().split())
one = list(sys.stdin.readline().strip())
two = list(sys.stdin.readline().strip())
t = int(sys.stdin.readline())

one.reverse()
arr = one + two
index = 0
while index < t:
    go = a-1-index
    if go < 0:
        go = index - a + 1
    break_flag = True
    while go < a + b - 1:
        flag = False
        if arr[go] in one:
            if arr[go + 1] in two:
                flag = True
                arr[go], arr[go + 1] = arr[go + 1], arr[go]
        elif arr[go] in two:
            if arr[go + 1] in one:
                flag = True
                arr[go], arr[go + 1] = arr[go + 1], arr[go]

        if flag:
            go += 2
            break_flag = False
        else:
            go += 1

    if break_flag:
        break

    index += 1

print(''.join(arr))
