# baekjoon source = "https://www.acmicpc.net/problem/2675"

import sys
import math

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

x = B/D
y = A/C
L = L - max(x,y)
print(math.floor(L))