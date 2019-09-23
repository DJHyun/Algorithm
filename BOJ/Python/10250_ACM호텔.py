# baekjoon source = "https://www.acmicpc.net/problem/10250"

import sys

T = sys.stdin.readline().strip()

for test in range(int(T)):
    hwn = list(map(int, sys.stdin.readline().strip().split()))
    h, w, n = hwn[0], hwn[1], hwn[2]
    result = ''

    num = n // h
    d = n % h

    if d == 0:
        if num < 10:
            result = str(h) + str(0) + str(num)
        else:
            result = str(h) + str(num)
    else:
        if (num + 1) <= 9:
            result = str(d) + str(0) + str(num + 1)
        else:
            result = str(d) + str(num + 1)

    print(result)
