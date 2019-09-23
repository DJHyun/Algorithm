# baekjoon source = "https://www.acmicpc.net/problem/2522"

import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline()
c = 0

for i in range(3):
    d = a*int(b[2-i])
    print(d)
    c += d*10**i

print(c)
