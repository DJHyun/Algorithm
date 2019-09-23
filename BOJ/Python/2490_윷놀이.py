# baekjoon source = "https://www.acmicpc.net/problem/2490"

import sys

for _ in range(3):
    check = list(map(int,sys.stdin.readline().split()))

    if check.count(0) == 4:
        print('D')
    elif check.count(0) == 3:
        print('C')
    elif check.count(0) == 2:
        print('B')
    elif check.count(0) == 1:
        print('A')
    else:
        print('E')