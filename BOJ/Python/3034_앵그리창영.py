# baekjoon source = "https://www.acmicpc.net/problem/3034"

import sys
import math

n, w, h = map(int, sys.stdin.readline().split())
a = math.sqrt(w ** 2 + h ** 2)

for i in range(n):
    check = int(sys.stdin.readline())
    if check <= w or check <= h or check <= a:
        print('DA')
    else:
        print('NE')
