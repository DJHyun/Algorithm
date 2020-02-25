# baekjoon source = "https://www.acmicpc.net/problem/1904"

import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a = 1
    b = 2
    index = 2
    while index < n:
        index += 1
        a,b = b, a+b
    print(b%15746)