# baekjoon source = "https://www.acmicpc.net/problem/2869"

import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
if a == b:
    print(1)
else:
    print(math.ceil((v - a) / (a - b)) + 1)
