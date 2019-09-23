# baekjoon source = "https://www.acmicpc.net/problem/2935"

import sys

a = int(sys.stdin.readline())
cen = sys.stdin.readline().strip()
b = int(sys.stdin.readline())

if cen == '+':
    print(a+b)
else:
    print(a*b)